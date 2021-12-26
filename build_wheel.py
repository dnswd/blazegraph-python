import subprocess
import sys

def install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "wheel"])
    subprocess.check_call([sys.executable, "-m", "python", "setup.py", "bdist_wheel"])

if __name__ == "__main__":
  install()