from django.http import HttpResponse

from ..module.auzerConnect import Auzer;

class torrent:
    @staticmethod
    def getTorrent(request):
        rows = Auzer.QueryExecute("select * from Title");
        ret = "";
        for row in rows:
            ret = str(row[0]) + row[1];        
        return HttpResponse(ret);