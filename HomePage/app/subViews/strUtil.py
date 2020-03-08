import re
class strUtil:
 tvPattern = 0
 movePattern = 0

 @staticmethod
 def init():
  strUtil.titlePattern = '.+.E\d+' 
 @staticmethod
 def isMatchTitle(title):
  strUtil.init();
  if(re.search(strUtil.titlePattern,title)):
    return True
  return False

 @staticmethod
 def getRegulaString(str, pattern):
  regulTitle = re.compile(pattern)
  result = regulTitle.findall(str)
  return result;

 @staticmethod
 def getMatchTitle(title):
  strUtil.init()
  
  result = strUtil.getRegulaString(title, strUtil.titlePattern);
  length = len(result);
  if(0 != length):
   return result[length - 1];
  return title;

