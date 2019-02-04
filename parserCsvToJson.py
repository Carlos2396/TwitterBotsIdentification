import csv, sys, requests, json

def main():
    if len(sys.argv) != 3:
        return
    in_name = sys.argv[1]
    out_name = sys.argv[2]

    with open(in_name, mode='r') as read_file:
        reader = csv.DictReader(read_file)
        success = []
        failed = []
        counter = 0

        for row in reader:
            data = {}
            data['id'] = counter
            data['isBot'] = (int)(row['Class']) == 1

            try:
                text = row['Tweet'].encode('latin-1', 'ignore').decode('latin-1')
                data['text'] = text
                success.append(data)
            except UnicodeEncodeError as ex:
                data['text'] = row['Tweet']
                failed.append(data)

            counter += 1
        
        with open('errors.csv', 'w') as errorFile:
            writer = csv.writer(errorFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for data in failed:
                writer.writerow([data['id'], data['text'], data['isBot']])

        with open(sys.argv[2], 'w') as outfile:
            json.dump(success, outfile)

if __name__ == '__main__':
    main()