import json, sys, re

def main():
    if len(sys.argv) != 4:
        return
        
    inname = sys.argv[1]
    inname2 = sys.argv[2]
    outname = sys.argv[3]

    with open(inname, mode='r') as inFile:
        with open(inname2, mode='r') as inFile2:
            oldT = json.load(inFile)
            newT = json.load(inFile2)
            
            for f in oldT:
                for s in newT: 
                    f.update(s)

            with open(outname, 'w') as outfile:
                json.dump(oldT, outfile)

if __name__ == '__main__':
    main()