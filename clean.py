import json, sys, re

def main():
    if len(sys.argv) != 3:
        return
        
    inname = sys.argv[1]
    outname = sys.argv[2]

    langs = {'es', 'en', 'fr', 'de', 'ja', 'ar', 'ch', 'nl', 'it', 'ko', 'pt', 'ru'}

    with open(inname, mode='r') as inFile:
        tweets = json.load(inFile)
        keysToClean = set(tweets[0].keys()) - {'words', 'links', 'text', 'hashtags', 'id', 'isRetweet', 'lang', 'mentions'}

        for tweet in tweets:
            if tweet['lang'] not in langs:
                for key in keysToClean:
                    tweet[key] = None
            
            tweet['words'] = tweet['words'] - tweet['mentions'] - tweet['links'] - tweet['hashtags']
            if tweet['isRetweet']:
                tweet['words'] -= 1 

        with open(outname, 'w') as outfile:
            json.dump(tweets, outfile)

if __name__ == '__main__':
    main()