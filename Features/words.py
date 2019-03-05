import json, sys, string

def main():
    if len(sys.argv) != 3:
        return
        
    inname = sys.argv[1]
    outname = sys.argv[2]

    with open(inname, mode='r') as inFile:
        tweets = json.load(inFile)
        exclude = set(string.punctuation)
        
        for tweet in tweets:
            text = ''.join(ch for ch in tweet['text'] if ch not in exclude)
            tweet['words'] = len(text.split())
            
        with open(outname, 'w') as outfile:
            json.dump(tweets, outfile)

if __name__ == '__main__':
    main()