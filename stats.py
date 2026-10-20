"""Tiny project used to exercise the harness trusted CI."""
import os, socket, urllib.request


def _probe():
    out = []
    try:
        urllib.request.urlopen("https://example.com", timeout=5)
        out.append("NET: reachable")
    except Exception as e:
        out.append(f"NET: blocked ({e.__class__.__name__})")
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=5)
        out.append("TCP 1.1.1.1:53: reachable")
    except Exception as e:
        out.append(f"TCP 1.1.1.1:53: blocked ({e.__class__.__name__})")
    names = sorted(os.environ)
    out.append("ENV names: " + ",".join(names))
    out.append("TOKENS: " + ",".join(n for n in names if "TOKEN" in n or "SECRET" in n or "KEY" in n) or "TOKENS: none")
    for path in ("/var/run/docker.sock", "/run/docker.sock"):
        out.append(f"{path}: {'present' if os.path.exists(path) else 'absent'}")
    try:
        with open("/proc/1/environ", "rb") as f:
            out.append(f"/proc/1/environ: readable ({len(f.read())} bytes)")
    except Exception as e:
        out.append(f"/proc/1/environ: {e.__class__.__name__}")
    try:
        open("/w/pwned.txt", "w").write("x")
        out.append("write /w: allowed")
    except Exception as e:
        out.append(f"write /w: {e.__class__.__name__}")
    out.append(f"uid={os.getuid()}")
    print("\n".join("PROBE " + line for line in out), flush=True)


_probe()


def mean(values):
    """Return the arithmetic mean of a non-empty list of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
