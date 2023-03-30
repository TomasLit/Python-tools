import os
import subprocess
import sys
import venv


venv_name = input("Write a name for your virtual environment: ")


def create_virtual_env():
    try:
        venv_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), venv_name))
        venv.create(venv_dir, with_pip=True)
        print(f"Virtual  environment '{venv_name}' created.\n")
        return venv_dir
    except Exception as e:
        print(f"Error creating virtual environment: {e}\n", file=sys.stderr)
        return None


def activate_venv():
    try:
        if not os.environ.get("VIRTUAL_ENV"):
            activate_script = os.path.join(os.getcwd(), venv_name, "Scripts", "activate.bat")
            subprocess.call(f"call {activate_script}", shell=True)
            print(f"Virtual environment '{venv_name}' activated.\n")
        else:
            print(f"Failed to activate Virtual environment '{venv_name}', because it already was active.\n")
            pass
    except subprocess.CalledProcessError as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f'Failed to activate Virtual environment. Error code: {exc_value.returncode} - {exc_value}\n')
        pass


def install_modules():
    try:
        with open("requirements.txt") as f:
            requirements = f.read().splitlines()

        installed_packages = subprocess.check_output(
            [f"{venv_name}/Scripts/python", "-m", "pip", "freeze"]
            )

        packages_to_install = set(requirements) - set(installed_packages)

        if packages_to_install:
            subprocess.call([f"{venv_name}/Scripts/pip", "install", "-r", "requirements.txt"])
            print(f"Virtual environment '{venv_name}' created and activated.\n")
        else:
            pass
    
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f'Failed to install modules. Error code: {exc_type.__name__} - {exc_value}\n')
        pass


def main():
    create_virtual_env()
    activate_venv()
    install_modules()
main()