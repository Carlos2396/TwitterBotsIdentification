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
            writer = csv.DictWriter(csvFile, tweets[0].keys())
            writer.writeheader()

            for tweet in tweets:
                writer.writerow(tweet)

if __name__ == '__main__':
    main()