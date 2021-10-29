import glob
import subprocess


if __name__ == "__main__":
    for py_script in glob.glob("**/*.py", recursive=True):
        print("checking %s..." % py_script)
        _ = subprocess.run(
            "mypy --strict --ignore-missing-imports %s" % py_script,
            shell=True,
        )
