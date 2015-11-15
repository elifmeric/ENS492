import re
from collections import Counter
import codecs
for year in range(1947,2015):
    file3 = codecs.open("words-"+str(year)+".txt", "w", encoding='utf8')


    def openfile(filename):
        fl = open(filename, "r+")
        str = fl.read()
        fl.close()
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

    def main(filename, freq):
        text = openfile(filename)
        text = removegarbage(txt)
        words = text.split(' ')
        bin = getwordbins(words)
        for key, value in bin.most_common(freq):
            print key,value
            file3.write(unicode(key) + " " + unicode(value) + "\n")
        

    main("lyrics" + unicode(year) + ".txt", 500)

    

