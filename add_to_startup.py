import os
import sys
import shutil

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    with open(os.path.join(bat_path, "open_flask_app.bat"), "w+") as bat_file:
        bat_file.write(r'start "" "{}\run_app.py"'.format(file_path))

if __name__ == "__main__":
    add_to_startup()
