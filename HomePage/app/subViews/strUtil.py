import re
class strUtil:
 tvPattern = 0
 movePattern = 0

 @staticmethod
 def init():
  strUtil.tvPattern = '[ ㄱ-ㅎ|가-힣]+.E\d\d'
  strUtil.movePattern = '[ ㄱ-ㅎ|가-힣]+'
 
 @staticmethod
 def isMatchTitle(title):
  strUtil.init();
  if(re.search(strUtil.movePattern,title)):
   return True
  if(re.search(strUtil.tvPattern, title)):
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
  
  result = strUtil.getRegulaString(title, strUtil.tvPattern);
  length = len(result);
  if(0 != length):
   return result[length - 1];

  result = strUtil.getRegulaString(title, strUtil.movePattern)
  if([] != result):
   return result[0];
  return title;
#  return re.compile('[ㄱ-|가-힣]', title);
