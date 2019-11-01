import re
class strUtil:
 @staticmethod
 def isMatchTitle(title):
  if(re.search('[ㄱ-ㅎ|가-힣]',title)):
   return True;
  return False;

 @staticmethod
 def getMatchTitle(title):
  regulTitle = re.compile('[^ㄱ-ㅎ|가-힣].E');
  result = regulTitle.sub('',title);
  return result;
#  return re.compile('[ㄱ-|가-힣]', title);
