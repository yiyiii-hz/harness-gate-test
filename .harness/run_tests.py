"""可信 CI 的测试运行脚本（base 拥有，候选不能修改）。

用法：python -P run_tests.py <代码根目录> <测试目录>

- 用 -P 启动，当前目录不进 sys.path；代码根目录追加在标准库之后，
  候选放一个 unittest.py 之类的同名文件也顶替不了标准库。
- 按文件路径加载测试，不用 unittest discover（它会把顶层目录插到 sys.path 最前面）。
- 最后一行打印结果行，宿主步骤据此核对跑了几个测试。
"""
import importlib.util
import pathlib
import sys
import unittest

root, tests_dir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
sys.path.append(str(root))

suite = unittest.TestSuite()
for i, path in enumerate(sorted(tests_dir.glob("test_*.py"))):
    spec = importlib.util.spec_from_file_location(f"harness_test_{i}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(module))

result = unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)
print(f"HARNESS-RESULT ran={result.testsRun} failures={len(result.failures)} "
      f"errors={len(result.errors)} skipped={len(result.skipped)}", flush=True)
sys.exit(0 if result.wasSuccessful() and result.testsRun > 0 else 1)
