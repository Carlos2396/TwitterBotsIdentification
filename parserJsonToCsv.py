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
            del tweets[0]["id"]
            writer = csv.DictWriter(csvFile, tweets[0].keys())
            writer.writeheader()

            first = True
            for tweet in tweets:
                if first:
                    first = False
                else:
                    del tweet["id"]
                tweet["text"] = "\"%s" % (tweet["text"])
                writer.writerow(tweet)

if __name__ == '__main__':
    main()