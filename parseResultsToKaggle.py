import csv, sys

def main():
    if len(sys.argv) != 2:
        return

    in_name = sys.argv[1]

    with open(in_name, mode='rw') as read_file:
        reader = csv.DictReader(read_file)
        tweets = []

        for row in reader:
            data = {}
            data['Id'] = row['inst#']
            data['Expected'] = 1 if (row['predicted']) == "1:Bot" else 0
            tweets.append(data)

        with open(in_name, 'w') as csvFile:
            writer = csv.DictWriter(csvFile, tweets[0].keys())
            writer.writeheader()

            for tweet in tweets:
                writer.writerow(tweet)

if __name__ == '__main__':
    main()