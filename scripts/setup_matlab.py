import os
import os.path as op
import platform
import subprocess
import sys
import urllib.request
import zipfile
from itertools import product
import tempfile
import argparse

def add_matlab_to_path(matlab_version) -> bool:
    """Detect default MATLAB installation path based on the platform."""
    system = platform.system().lower()

    paths = [
        'runtime', 
        'bin',
        'sys/os',
        'extern/bin',
    ]

    if system == "windows":
        variable = 'PATH'
        bases = [
            f"C:/Program Files/MATLAB/{matlab_version}", 
            f"C:/Program Files (x86)/MATLAB/{matlab_version}", 
            f"C:/Program Files/MATLAB/MATLAB Runtime/{matlab_version}", 
            f"C:/Program Files (x86)/MATLAB/MATLAB Runtime/{matlab_version}", 
        ]
        archs = ['win32', 'win64']

    elif system == "darwin":  # macOS
        variable = 'DYLD_LIBRARY_PATH'
        bases = [
            f"/Applications/MATLAB_{matlab_version}",
            f"/Applications/MATLAB_Runtime/{matlab_version}"
        ]

        if platform.processor() == 'i386':
            archs = ['maci64']
        else:
            archs = ['maca64']

    elif system == "linux":
        variable = 'LD_LIBRARY_PATH'
        bases = [
            f"/usr/local/MATLAB/{matlab_version}",
            f"/usr/local/MATLAB/MATLAB_Runtime/{matlab_version}",
        ]
        archs = ['glnxa64']

    envpath = os.environ.get(variable, "")
    found = False
    for base, path in product(bases, paths):
        # Check path existence
        check_path = op.join(base, path)
        if op.exists(check_path):
            print(f"{check_path}")
            found = True
        else: 
            continue

        # Add to the environment variables
        for arch in archs:
            fullpath = op.join(check_path, arch)
            if fullpath not in envpath:
                envpath = f"{fullpath}{os.pathsep}{envpath}"

        # Break
        if found: 
            break


    os.environ[variable] = envpath

    return found
    

def try_import(module_name):
    """Try importing a module and return success status."""
    try:
        subprocess.check_call(['python', '-c', '"import spm;exit(0)"'])
        return True
    except:
        return False

def download_matlab_runtime(system):
    base_url = "https://github.com/spm/spm/releases/download/25.01.alpha42/"

    if system == "windows":
        zip_name = 'spm_standalone_25.01.alpha42_Windows_matlab_runtime_installer.zip'

    elif system == "darwin":  # macOS

        if platform.processor() == 'i386':
            zip_name = 'spm_standalone_25.01.alpha42_macOS_Intel_matlab_runtime_installer.zip'
        else:
            zip_name = 'spm_standalone_25.01.alpha42_macOS_Apple_Silicon_matlab_runtime_installer.zip'

    elif system == "linux":
        zip_name = 'spm_standalone_25.01.alpha42_Linux_matlab_runtime_installer.zip'

    runtime_url = op.join(base_url, zip_name)

    dest_folder = tempfile.mkdtemp()

    zip_file_path = op.join(dest_folder, zip_name)
    print(f"Downloading MATLAB Runtime from {runtime_url}...")
    urllib.request.urlretrieve(runtime_url, zip_file_path)

    print("Extracting MATLAB Runtime...")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)

    installer_path = op.join(dest_folder, "runtime_installer")

    return installer_path, dest_folder

def download_and_install_matlab_runtime():
    """Download and install MATLAB Runtime."""

    system = platform.system().lower()

    installer_path, dest_folder = download_matlab_runtime(system)

    os.chdir(installer_path)
    installer_file = os.listdir(installer_path)[0]

    if system == 'linux' or system == 'darwin':
        subprocess.check_call(['chmod', 'u+x', installer_file])

        installer_file = op.join('.', installer_file)

    command = [installer_file, '-agreeToLicense', 'yes']
    
    success = False
    try:
        subprocess.check_call(command)
        success = True

    except PermissionError as e:
        print(f"Permission error during installation: {e}")

    except Exception as e:
        print(f'Command {command} raised:\n')
        print(e)

    return success

def setup_matlab_environment(download):
    """Main function to set up MATLAB or MATLAB Runtime."""
    module_name = "spm"

    # Try importing the module
    if try_import(module_name):
        return True

    runtime_found = add_matlab_to_path('R2024b')

    if runtime_found and try_import(module_name):
        return True

    if not download:
        ans = input("MATLAB Runtime not found, do you want to download it? (y/n) ")

        if ans.lower() != 'y':
            raise ImportError(f"Failed to import {module_name}. Please check your setup.")

    runtime_installed = download_and_install_matlab_runtime()

    if not runtime_installed:
        raise SystemError(f'Failed to install Matlab Runtime. Please try manually.')

    runtime_found = add_matlab_to_path('R2024b')

    if runtime_found and try_import(module_name):
        return True 
    else:
        raise ImportError(f"Failed to import {module_name}. Please check your setup.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='setup_matlab')
    parser.add_argument('-d', '--download-if-not-found', dest='download', action='store_true')
    parser.add_argument('-p', '--print', dest='print', action='store_true')
    args = parser.parse_args()

    if args.print: 
        add_matlab_to_path("R2024b")
        exit(0)
    else:    
        result = setup_matlab_environment(args.download)
        if result:
            exit(0)
        else:
            exit(-1)
