import subprocess


def flatten_dict(d: dict):
    l = []
    for item in d.items():
        l.extend(item)
    l = list(filter(lambda obj: obj is not None, l))
    return l


def execute(name: str, args: dict, kwargs: dict, cwd):
    base = ["python", "-m", "scripts." + name]
    cmd = base + list(args.values()) + flatten_dict(kwargs)
    try:
        out = subprocess.run(cmd, cwd=cwd)
    except KeyboardInterrupt:
        print("Aborted!")
    except FileExistsError:
        print("Output directory is not empty!")
    except Exception:
        print("Unexpected error!")
        print(out)
