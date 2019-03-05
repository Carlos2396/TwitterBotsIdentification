import json, sys

def main():
    if len(sys.argv) != 3:
        return
        
    inname = sys.argv[1]
    outname = sys.argv[2]

    with open(inname, mode='r') as inFile:
        tweets = json.load(inFile)

        for tweet in tweets:
            tweet['isRetweet'] = "RT @" in tweet['text']
            
        with open(outname, 'w') as outfile:
            json.dump(tweets, outfile)

if __name__ == '__main__':
    main()