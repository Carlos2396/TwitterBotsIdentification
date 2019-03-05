import indicoio, json, sys

indicoio.config.api_key = '9f1dbd8b60857ed8ac6c10e441772edc'

def main():
    if len(sys.argv) != 3:
        return
        
    inname = sys.argv[1]
    outname = sys.argv[2]

    with open(inname, mode='r') as inFile:
        tweets = json.load(inFile)
        count = 0

        for tweet in tweets:
            result = indicoio.emotion(tweet['text'])
            tweet['anger'] = result['anger']
            tweet['joy'] = result['joy']
            tweet['fear'] = result['fear']
            tweet['sadness'] = result['sadness']
            tweet['surprise'] = result['surprise']

            count += 1

            if count % 100 == 0:
                print(count)
                with open(outname, 'w') as outfile:
                    json.dump(tweets, outfile)
        
        with open(outname, 'w') as outfile:
            json.dump(tweets, outfile)
            

if __name__ == '__main__':
    main()