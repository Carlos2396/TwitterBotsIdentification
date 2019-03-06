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
            result = indicoio.text_tags(tweet['text'])
            tweet['topic'] = getTopic(result)
            count += 1

            if count % 100 == 0:
                print(count)
                with open(outname, 'w') as outfile:
                    json.dump(tweets, outfile)
        
        with open(outname, 'w') as outfile:
            json.dump(tweets, outfile)
            
def getTopic(topics):
    max = 0
    for topic in topics.keys():
        if topics[topic] > max:
            max = topics[topic]
            top = topic

    return top

if __name__ == '__main__':
    main()