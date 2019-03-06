import csv, sys, json

def main():
    if len(sys.argv) != 3:
        return
        
    jsonName = sys.argv[1]
    csvName = sys.argv[2]

    with open(jsonName, mode='r') as jsonFile:
        tweets = json.load(jsonFile)
        if len(tweets) == 0:
            return

        with open(csvName, 'w') as csvFile:
            keys = set(tweets[0].keys()) - set(['class', 'id'])
            keys = sorted(keys)
            keys.append('class')

            writer = csv.DictWriter(csvFile, keys)
            writer.writeheader()

            for tweet in tweets:
                del tweet['id']
                if "class" not in tweet:
                    tweet["class"] = "?"
                
                tweet["text"] = "\"%s" % (tweet["text"].encode('utf8', 'ignore'))
                writer.writerow(tweet)

if __name__ == '__main__':
    main()