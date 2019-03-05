import json, sys

def main():
    if len(sys.argv) != 3:
        return
        
    inname = sys.argv[1]
    outname = sys.argv[2]

    with open(inname, mode='r') as inFile:
        tweets = json.load(inFile)

        for tweet in tweets:
            tweet['mentions'] = countMentions(tweet['text'])
            
        with open(outname, 'w') as outfile:
            json.dump(tweets, outfile)
            
def countMentions(text):
    count = 0
    for i in range(len(text)):
        if text[i] == '@':
            if i < len(text)-1 and text[i+1] != ' ':
                count += 1
    
    return count


if __name__ == '__main__':
    main()