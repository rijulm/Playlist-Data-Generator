# file to analyse text file and generate test data
# rijul 25/4/20
import re
import pandas
import copy


def readTxtFile(name):
    # function to read the text file and return an array with all of it 
    with open(name) as f:
        lines = f.read().splitlines()
    return lines


def getIntros(lines):
    # function to separate all the intros
    intro = []
    for elem in lines:
        intro.append(elem.split('{')[0])
    return list(set(intro))


def getSongNames(lines):
    # function to get all the info of the song_names type
    song_names = []
    for elem in lines:
        temp = getTypeInfo(elem)
        for elem2 in temp:
            if "song_name" in elem2:
                song_names.append("{"+elem2+"}")
    return list(set(song_names))

def getArtists(lines):
    # function to get all the info of the artist type
    artists = []
    for elem in lines:
        temp = getTypeInfo(elem)
        for elem2 in temp:
            if "artist" in elem2:
                artists.append("{"+elem2+"}")
    return list(set(artists))


def getTypeInfo(string):
    # this function will take a string and return whatever is inside the {}
    return re.findall(r"\{(.*?)\}", string)

def getExits(lines):
    # function to separate all the intros
    exit = []
    for elem in lines:
        exit.append(elem.split('}')[-1])
    return list(set(exit))

def final(intros , exits, song_names, artists):
    import random
    for i in range(30):
        print(random.choice(intros) + random.choice(song_names) + " by " + random.choice(artists))
        if i%2==0:
            print(random.choice(intros) + random.choice(song_names) + " by " + random.choice(artists) + random.choice(exits))

# adding further support for reading from the csv file and generating a dictionary and array
def csvToList(fileName):
    csvfile = pandas.read_csv(fileName)
    finalDict = {}
    for item in (csvfile['Zip']):
        finalDict[item] = ""

    for i in range(len(csvfile)):
        # print(csvfile['Zip'])
        # if csvfile['country'][i] == "United States":
        # finalDict[csvfile['City'][i]] = ""
        continue

    # print(finalDict)
    return finalDict

def getUniqueItems(d):
    pass

    # result = []
    # for key, values in d.items():
    #     result.append((key, values))
    #
    # result = list(set([i for i in result]))
    #
    # final = {}
    # for item in result:
    #     final[item[0]] = item[1]

    # mn = list(b.keys())
    # other = list(final_places.keys())
    #
    # new_b = copy.deepcopy(b)
    #
    # common = []
    # for thing in mn:
    #     if thing in other:
    #         if final_places[thing] == b[thing]:
    #             common.append(thing)
    #             del new_b[thing]
    #
    # print(len(common))
    # print(len(new_b))
    #
    # return new_b

if __name__ == '__main__':
    a = csvToList('mn cities.csv')
    b = getUniqueItems(a)
    print(b)


