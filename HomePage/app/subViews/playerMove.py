from django.http import HttpResponse
from ..module.osDefine import osDefine
class playerMove():

    @staticmethod
    def Back600(param):
        osDefine.Skip(-300)
        return HttpResponse("Back 600s")

    @staticmethod
    def Back(param):
        osDefine.Skip(-30)
        return HttpResponse("back 10s")

    @staticmethod
    def Replay(param):
        osDefine.Replay(param)
        return HttpResponse("Replay")

    @staticmethod
    def Pause(param):
        osDefine.Pause(param)
        return HttpResponse("Pause")

    @staticmethod
    def Pause(param):
        osDefine.Pause(param)
        return HttpResponse("Pause")
    
    @staticmethod
    def Stop(param):
        osDefine.Stop(param)
        return HttpResponse("Pause")

    @staticmethod
    def Skip(param):
        osDefine.Skip(30)
        return HttpResponse("skip 10s")

    @staticmethod
    def Skip600(param):
        osDefine.Skip(300)
        return HttpResponse("Skip 600s")
    
    @staticmethod
    def VolumeUp(param):
        osDefine.Action(18)
        return HttpResponse("Volume Up")

    @staticmethod 
    def VolumeDown(param):
        osDefine.Action(17)
        return HttpResponse("Volume Down")

    @staticmethod 
    def CurFileName(param):
        return HttpResponse(osDefine.getPlayFileName())
 
