import os
import urllib.request
import subprocess
import time


def check_if_python_installed():
    python_installed = False
    try:
        subprocess.run(["python", "--version"], check=True)
        python_installed = True
    except subprocess.CalledProcessError:
        pass
    return python_installed

def download_and_install_python(python_installed):
    if not python_installed:
        version = "3.11.2"
        url = f"https://www.python.org/ftp/python/{version}/python-{version}-amd64.exe"
        urllib.request.urlretrieve(url, "python_installer.exe")

        print(f"Installing Python {version}...")
        subprocess.run(["python_installer.exe", "/quiet", "TargetDir=C:\\Python"], check=True)


def check_if_pip_installed():
    pip_installed = False
    try:
        subprocess.run(["pip", "--version"], check=True)
        pip_installed = True
    except subprocess.CalledProcessError:
        pass
    return pip_installed

def install_pip(pip_installed):
    if not pip_installed:
        print("Installing pip...")
        subprocess.run(["python", "-m", "ensurepip"], check=True)


def check_if_path_exists():
    python_path = os.getenv('PATH')
    python_path_added = False
    if python_path and "python" in python_path.lower():
        python_path_added = True
        print("PATH already exists!")
    return python_path_added

def create_python_path(python_path_added):
    if not python_path_added:
        print("Adding Python to PATH...")
        subprocess.run(["setx", "PATH", f"%PATH%;C:\\Python\\;C:\\Python\\Scripts"], check=True)


def main():
    download_and_install_python(check_if_python_installed())
    install_pip(check_if_pip_installed())
    create_python_path(check_if_path_exists())
    time.sleep(10)
main()