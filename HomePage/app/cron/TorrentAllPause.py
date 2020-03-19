import os;

def TorrentPauseAll():
    addCmd = "sudo transmission-remote -n \"pi\":\"cndwn5069()\" -t all --stop";
    os.system(addCmd);