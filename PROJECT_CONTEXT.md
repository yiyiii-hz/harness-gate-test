# 项目说明（PROJECT_CONTEXT）

审查时会把本文件（取自 main 分支）完整交给审查的 Claude。修改须经 PR，由用户合并。

## 这是什么
`harness-gate-test`：只用于测试 harness 流程的小项目，不含真实业务。核心代码是 `stats.py`，一组纯函数统计工具。

## 约定
- `stats.py` 只用标准库，不新增第三方依赖。依赖文件（`requirements.txt` 等）由可信 CI 保护，候选 PR 不能修改。
- 每个统计函数接收一个数字列表；列表为空时抛出 `ValueError("values must not be empty")`，与 `mean()` 保持一致。
- 每个函数都有一行英文 docstring，说明返回值和前提条件。
- 测试放在 `tests/test_*.py`，用 `unittest`。已有测试不能改、不能删，只能新增测试文件。

## 已知的坑
- `variance()` 是总体方差（除以 n），不是样本方差（除以 n-1）。新增相关函数时要在 docstring 里写清楚是哪一种。
- `median()` 对偶数长度返回中间两个数的平均值（可能是 float）。
- 根目录那些 `*.txt`、`hello.md`、`grok/`、`infra/` 是早期实验留下的占位文件，与代码无关，不要依赖它们。
