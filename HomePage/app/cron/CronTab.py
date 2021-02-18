import os

def PcReboot():
    os.system("sudo shutdown -r now")

def ServerRun():
    os.system("nohup sh /home/pi/Sylva/Pz/Run.sh &")

def Delete_DotVsCode():
    os.system("sudo rm -R '/home/pi/.vscode-server'")