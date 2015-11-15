import urllib2
import json
import codecs

api_key="80e5060e2c10c6d000cf7606229ae642"

file2 = codecs.open("somelyrics", "w", encoding='utf8')

for year in range(1947,2014):

    file2 = codecs.open("lyrics"+unicode(year)+".txt", "w", encoding='utf8')

    with open("ids-"+unicode(year)+".txt","r") as file:
    
        for line in file:
            line=line.strip()
            url="http://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id="+line+"&apikey={}".format(api_key)
            print url
            req = urllib2.Request(url)
            req.add_header("Accept", "application/json")
            response = urllib2.urlopen(req)
            data = json.loads(response.read())
                
        
            print data['message']['body']['lyrics']['lyrics_body']
            file2.write(unicode (data['message']['body']['lyrics']['lyrics_body']))