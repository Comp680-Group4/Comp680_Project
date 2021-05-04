import matplotlib.pyplot as plt
import numpy as np


def my_autopct(pct):
    return ('%.2f' % pct) if pct > 10 else ''

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
        words.append(word + ': ' + str(wordsDict[word]))
        if wordsDict[word] > prevLargest:
            prevLargest = wordsDict[word]
            posLargest = i
        i += 1

    for x in range(len(wordsDict)):
        if x == posLargest:
            myExplode.append(0.2)
        else:
            myExplode.append(0)

    percent = 100.*occurrences/occurrences.sum()

    patches, texts = plt.pie(occurrences, shadow=True, startangle=90, radius=1.2)
    labels = ['{0} - {1:1.2f} %'.format(i, j) for i, j in zip(words, percent)]

    sortLegend = True
    if sortLegend:
        patches, labels, dummy = zip(*sorted(zip(patches, labels, occurrences),
                                             key=lambda x: x[2],
                                             reverse=True))

    print(wordsDict)
    print(myExplode)
    plt.legend(patches, labels, loc='center', bbox_to_anchor=(-0.1, 1.), fontsize=8)
    #plt.pie(occurrences, labels=words, explode=myExplode, shadow=True)
    plt.show()