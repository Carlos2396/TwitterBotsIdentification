import csv, sys, requests, json, time

endpoint = "https://api.meaningcloud.com/sentiment-2.1"
key = "b8a6d3745e22b57811d6ffc7efef8ca9"

def main():
    if len(sys.argv) != 3:
        return
    inname = sys.argv[1]
    outname = sys.argv[2]

    with open(inname, mode='r') as inFile:
        tweets = json.load(inFile)
        counter = 0
        headers = {
            'content-type': 'application/x-www-form-urlencoded', 
            'charset': 'utf-8'
        }
        errors = []

        for tweet in tweets:
            if counter%50 == 0:
                print('Total: ', counter)
                with open(outname, 'w') as outfile:
                    json.dump(tweets, outfile)

            if 'confidence' in tweet.keys():
                counter += 1 
                continue
            else:
                time.sleep(.2)

            body = 'key=%s&lang=auto&ilang=en&txt=%s' % (key, tweet['text']) 
            res = requests.request("POST", endpoint, data=body.encode('latin-1', 'replace'), headers=headers)
            data = json.loads(res.text)

            if data['status']['msg'] == 'OK':
                tweet['isAgreement'] = data['agreement'] == "AGREEMENT"
                tweet['isSubjective'] = data['subjectivity'] == "SUBJECTIVE"
                tweet['isIronic'] = data['irony'] == "IRONIC"
                tweet['confidence'] = (int) (data['confidence'])
                tweet['polarity'] = getPolarityVal(data['score_tag'])
            else:
                data['id'] = counter
                errors.append(data)

            counter += 1

        with open(outname, 'w') as outfile:
            json.dump(tweets, outfile)

        with open('./Data/errors.json', 'w') as outfile:
            json.dump(errors, outfile)

            print(len(errors))

def getPolarityVal(value):
    switcher = {
        'N+': -2,
        'N': -1,
        'NONE': 0,
        'P': 1,
        'P+': 2
    }

    return switcher.get(value, 0)
    

if __name__ == '__main__':
    main()