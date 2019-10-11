from django.http import HttpResponse
from .osDefine import osDefine
class playerMove():
 @staticmethod
 def Skip(param):
  osDefine.Skip(10);
  return HttpResponse("skip 10s");


 @staticmethod
 def Back(param):
  osDefine.Skip(-10);
  return HttpResponse("back 10s");

 @staticmethod
 def VolumeUp(param):
  osDefine.Volume(1);
  return HttpResponse("Volume Up");

 @staticmethod 
 def VolumeDown(param):
  osDefine.Volume(-1);
  return HttpResponse("Volume Down");
 
