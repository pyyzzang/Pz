import os;

@staticmethod
def PcReboot():
    os.system("sudo shutdown -r now");

@staticmethod
def Delete_DotVsCode():
    os.system("sudo rm -R '/home/pi/.vscode-server'");