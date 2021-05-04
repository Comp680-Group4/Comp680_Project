import matplotlib.pyplot as plt
import numpy as np

def createPieGraph(wordsDict):
    #words = np.array([])
    #occurrences = []
    occurrences = np.array([])
    words = []
    myExplode = []
    prevLargest = 0
    posLargest = 0
    i = 0
    for word in wordsDict:
        #words = np.append(words, word)
        #occurrences.append(wordsDict[word])
        occurrences = np.append(occurrences, wordsDict[word])
        words.append(word)
        if wordsDict[word] > prevLargest:
            prevLargest = wordsDict[word]
            posLargest = i
        i += 1

    for x in range(len(wordsDict)):
        if x == posLargest:
            myExplode.append(0.2)
        else:
            myExplode.append(0)

    print(wordsDict)
    print(myExplode)
    plt.pie(occurrences, labels=words, explode=myExplode, shadow=True)
    plt.legend
    plt.show()
    z = "hi"