import os;

def PcReboot():
    os.system("sudo shutdown -r now");

def Delete_DotVsCode():
    os.system("sudo rm -R '/home/pi/.vscode-server'");