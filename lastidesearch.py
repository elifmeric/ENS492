import urllib2
import json
import codecs



api_key="80e5060e2c10c6d000cf7606229ae642"
#url="http://api.musixmatch.com/ws/1.1/matcher.lyrics.get?q_track=+unicode(q_track)+&q_artist=+unicode(q_artist)


count=0

for year in range(1947,2015):
        filename="year"+str(year)+".txt"
        file2 = codecs.open("ids-"+str(year)+".txt", "w", encoding='utf8')

        with open(filename) as file:
    
            for line in file:
                words=line.split('-')
                name=words[0]
                song=words[1]

                q_artist=name.replace(" ","%20")[0:-3]
                q_track=song.replace(" ","%20")[0:-1]
                url="http://api.musixmatch.com/ws/1.1/track.search?q_track="+unicode(q_track)+"&q_artist="+unicode(q_artist)+"&f_has_lyrics=1&apikey={}".format(api_key)
                req = urllib2.Request(url)
                req.add_header("Accept", "application/json")
                response = urllib2.urlopen(req)
                data = json.loads(response.read())
                
               
                if data['message']['header']['available']>0 :
                    count=count+1 
                    file2.write (unicode(data['message']['body']['track_list'][0]['track']['track_id'])+"\n")

            print count

                  
                    
             #   print "Available lyrics:  ", data['message']['header']['available']
               
                
               # file2.write(str(data))
                
                #print str(data)

 



