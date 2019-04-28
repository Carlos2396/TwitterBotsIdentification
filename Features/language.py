import json, sys, re
from langdetect import detect

def main():
    if len(sys.argv) != 3:
        return
        
    inname = sys.argv[1]
    outname = sys.argv[2]

    with open(inname, mode='r') as inFile:
        tweets = json.load(inFile)

        for tweet in tweets:
            try:
                tweet['lang'] = detect(tweet['text'])
            except:
                tweet['lang'] = None

        with open(outname, 'w') as outfile:
            json.dump(tweets, outfile)

if __name__ == '__main__':
    main()