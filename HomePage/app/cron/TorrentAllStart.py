import os


def TorrentAllStart():
    addCmd = "sudo transmission-remote -n \"pi\":\"cndwn5069()\" -t all --start";
    os.system(addCmd);
