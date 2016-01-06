from collections import Counter
import re
import codecs
for year in range(1947,1948):
    file3 = codecs.open("words-"+str(year)+".txt", "w", encoding='utf8')


    def openfile(filename):
        fh = open(filename, "r+")
        str = fh.read()
        fh.close()
        return str

    def removegarbage(str):
        # Replace one or more non-word (non-alphanumeric) chars with a space
        str = re.sub(r'\W+', ' ', str)
        str = str.lower()
	return str

    def getwordbins(words):
        cnt = Counter()
        for word in words:
            cnt[word] += 1
        return cnt

    def main(filename, topwords):
        txt = openfile(filename)
        txt = removegarbage(txt)
        words = txt.split(' ')
        bins = getwordbins(words)
        for key, value in bins.most_common(topwords):
            print key,value
            file3.write(unicode(key) + " " + unicode(value) + "\n")
        

    main("lyrics" + unicode(year) + ".txt", 500)

    

