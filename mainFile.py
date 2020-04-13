import math
import copy
#imports

#f = open("CS170_SMALLtestdata__74.txt", "r")
f = open("CS170_LARGEtestdata__76.txt", "r")
if f.mode == "r":
    data = f.readlines()
f.close()

val1 = input('Welcome to Geoffrey Nguyens searching algorithm! Please type the name of the file you want to enter:\n')
#if (val1 == 'CS170_SMALLtestdata__74.txt'):
if (val1 == 'CS170_LARGEtestdata__86.txt'):
    print(val1)
val2 = input('Type the number of the algorithm you want to run (1 for forward selection, 2 for backward elimination, 3 for my special algorithm):')

def distance(array1, array2):
    i = 1
    euclidDistance = 0
    for i in range(len(array1)):
        euclidDistance += math.pow(array1[i] - array2[i], 2)
        
    euclidDistance = math.sqrt(euclidDistance)
    return euclidDistance

i = 0
j = 0

newData = []

for i in range(len(data)):
    newArray = []
    splitting = data[i].split()
    
    for j in range(len(splitting)):
        newArray.append(float(splitting[j]))
    newData.append(newArray)

# k nearest neighbor: first, initialize minimum distance to distance between data and 1st array
# then, compare that minimum distance to the rest of the data
# if distance between data and nth array is LESS than current minimum distance, replace
# output should return last distance
# cross validation: leave one out


""" # never used
def kNearestNeighbor(newData, feature, set):
    i = 0
    j = 0
    count = 0
    for i in range(len(newData)):
        bestRow = []
        rowOfI = newData[i]
        minDistance = 100
        for j in range(len(newData)):
            rowOfJ = newData[j]
            if (i != j):
                if (minDistance > distance(rowOfI[1:], rowOfJ[1:])):
                    minDistance = distance(rowOfI[1:], rowOfJ[1:])
                    bestRow = rowOfJ
        # found min distance
        # now try to find accuracy
        if (bestRow[0] == rowOfI[0]):
            count += 1
    accuracy = count / len(newData)
    return accuracy
"""

# forward selection means you start off with no features and find the best feature after iterating through everything
# once you find the feature with the best accuracy, find another feature
# keep doing it until the accuracy goes down significantly

#WORKS, DO NOT CHANGE

def forwardSelection(newData):
    print('\n')
    print('Forward selection\n')
    i = 0
    j = 0
    a = 0
    rowOfBestDistance = newData[0]
    bestOverallAccuracy = 0
    bestOverallFeatures = []
    bestFeatures = []
    for a in range(1, len(newData[0])):                         
        bestCurrFeature = []
        bestCurrAccuracy = 0
        for x in range(1, len(newData[0])): # each feature      
            count = 0
            if (x not in bestOverallFeatures):
                for i in range(len(newData)): # validation row, value of newData is 300
                    rowI = newData[i] #ex: row 1
                    smallestCurrDistance = 100
                    for j in range(len(newData)): #tests against everything except validation row, value of newData is 300
                        rowJ = newData[j] #ex: row 2
                        if (i != j): # if row 1 != row 2
                            arr1, arr2 = [], []
                            for f in bestOverallFeatures:
                                arr1.append(rowI[f])
                                arr2.append(rowJ[f])
                            arr1.append(rowI[x])
                            arr2.append(rowJ[x])
                            if (smallestCurrDistance > distance(arr1, arr2)): #if the existing smallest distance is greater than the distance between feature X at I and feature X at J
                                smallestCurrDistance = distance(arr1, arr2)
                                rowOfBestDistance = rowJ # the row at which it was founded at
                            #closing if
                        #closing if
                    #closing for
                    if (rowOfBestDistance[0] == rowI[0]):
                        count += 1
            #closing for
            #total number of times it was accurate for feature X
                kNNaccuracy = count / len(newData) # 0.683333
                print('This is kNN accuracy at', x, ':', kNNaccuracy)
                if (bestCurrAccuracy < kNNaccuracy):
                    bestCurrAccuracy = kNNaccuracy
                    bestCurrFeature = x
        if (bestOverallAccuracy < bestCurrAccuracy):
            #print('Best overall accuracy is now', bestCurrAccuracy)
            bestOverallAccuracy = bestCurrAccuracy
            bestFeatures.append(bestCurrFeature)
        bestOverallFeatures.append(bestCurrFeature)
        print('Best overall features are: ', bestOverallFeatures, 'with a feature accuracy of', bestOverallAccuracy)
        #closing for
    #closing for


    print('Best overall accuracy is ', bestOverallAccuracy, 'with features', bestFeatures)

    print('Last current accuracy percentage is', bestCurrAccuracy)
    return(bestCurrAccuracy)




# backward elimination is adding all of the features first, and then removing the ones that are useless
# compute distance of all features first, remove the most distant one, then run again without the most distant one
# repeat until distance is lower accuracy than independent features

# this function calculates the initial value with all 10 features
def backwardElimination(newData):
    print('\n')
    print('Backward elimination\n')
    allFeatAccuracy = 0
    count = 0
    b = 0
    for b in range(len(newData)):
        baseAcc = 100
        rowB = newData[b]
        for k in range(len(newData)):
            rowK = newData[k]
            if b != k:
                if distance(rowB[1:], rowK[1:]) < baseAcc:
                    baseAcc = distance(rowB[1:], rowK[1:])
                    rowBestDistance = rowK
        if (rowB[0] == rowBestDistance[0]):
            count += 1
    allFeatAccuracy = count / len(newData)

    # actual backward elimination
    i = 0
    j = 0
    a = 0
    rowOfBestDistance = newData[0]
    bestOverallAccuracy = allFeatAccuracy
    bestOverallFeatures = []  
    featuresInArray = []
    featureToRemove = 0

    for z in range(1, len(newData[0])):
        featuresInArray.append(z)

    print('For backward selection, the current array is', featuresInArray, 'with an accuracy of', allFeatAccuracy)

    for a in range(1, len(newData[0])):
        print('After the', a, 'th iteration:')                      
        bestCurrAccuracy = 0
        for x in range(1, len(newData[0])): # each feature      
            count = 0
            if (x in featuresInArray):
                for i in range(len(newData)): # validation row, value of newData is 300
                    rowI = newData[i] #ex: row 1
                    smallestCurrDistance = 100
                    #biggestCurrDistance = 0
                    for j in range(len(newData)): #tests against everything except validation row, value of newData is 300
                        rowJ = newData[j] #ex: row 2
                        if (i != j): # if row 1 != row 2
                            arr1, arr2 = [], []
                            for f in featuresInArray:
                                arr1.append(rowI[f])
                                arr2.append(rowJ[f])
                            arr1.remove(rowI[x])
                            arr2.remove(rowJ[x])
                            if (smallestCurrDistance > distance(arr1, arr2)): #if the existing smallest distance is greater than the distance between feature X at I and feature X at J
                                smallestCurrDistance = distance(arr1, arr2)
                                rowOfBestDistance = rowJ # the row at which it was founded at
                            #closing if
                        #closing if
                    #closing for
                    if (rowOfBestDistance[0] == rowI[0]):
                        count += 1
            #closing for
            #total number of times it was accurate for feature X
                kNNaccuracy = count / len(newData) # 0.683333
                #print('This is kNN accuracy at', x, ':', kNNaccuracy)
                if (bestCurrAccuracy < kNNaccuracy):
                    bestCurrAccuracy = kNNaccuracy
                    featureToRemove = x
        featuresInArray.remove(featureToRemove)
        if (bestOverallAccuracy < bestCurrAccuracy):
            #print('Best overall accuracy is now', bestCurrAccuracy)
            bestOverallAccuracy = bestCurrAccuracy
            bestOverallFeatures = copy.deepcopy(featuresInArray)
            print('Best overall features: ', bestOverallFeatures)
        #featuresInArray.remove(featureToRemove)
        #bestFeatures.append(bestCurrFeature)
        #featuresInArray.remove(featureToRemove)
        print('Features in the array are now', featuresInArray, 'with an accuracy of', bestCurrAccuracy)
        #print('Best overall features are: ', featuresInArray)
        #closing for
    #closing for
    #print('Now, the current feature list is', featuresInArray, 'with an accuracy of', allFeatAccuracy)
    print('The best overall accuracy was', bestOverallAccuracy, 'with features', bestOverallFeatures)
    return(bestOverallAccuracy)


# bi directional search uses both forward selection and backward elimination to find the answer
# once both searches have the same features, you found your goal node and succeed


def biDirectional(newData):
    print('\n')
    print('Bi-directional search\n')
    allFeatAccuracy = 0
    count = 0
    b = 0
    for b in range(len(newData)):
        baseAcc = 100
        rowB = newData[b]
        for k in range(len(newData)):
            rowK = newData[k]
            if b != k:
                if distance(rowB[1:], rowK[1:]) < baseAcc:
                    baseAcc = distance(rowB[1:], rowK[1:])
                    rowBestDistance = rowK
        if (rowB[0] == rowBestDistance[0]):
            count += 1
    allFeatAccuracy = count / len(newData)

    i = 0
    j = 0
    a = 0
    bestFeatureValueFS = 0
    rowOfBestDistanceFS = newData[0]
    rowOfBestDistanceBE = newData[0]
    bestOverallAccuracyFS = 0
    bestOverallAccuracyBE = allFeatAccuracy
    bestOverallFeaturesFS = []
    bestOverallFeaturesBE = []
    bestFeatures = []
    featuresInArray = []
    featureToRemove = 0


    halfNewDataArray = len(newData[0]) / 2 + 1
    halfNewDataArray = int(halfNewDataArray)

    for z in range(1, len(newData[0])):
        featuresInArray.append(z)

    for a in range(1, halfNewDataArray):                         
        bestCurrFeature = []
        bestCurrAccuracyFS = 0
        bestCurrAccuracyBE = 0
        for x in range(1, len(newData[0])): # each feature

            # forward selection

            countForFS = 0
            if (x not in bestOverallFeaturesFS):
                for i in range(len(newData)): # validation row, value of newData is 300
                    rowI = newData[i] #ex: row 1
                    smallestCurrDistanceFS = 100
                    for j in range(len(newData)): #tests against everything except validation row, value of newData is 300
                        rowJ = newData[j] #ex: row 2
                        if (i != j): # if row 1 != row 2
                            arr1, arr2 = [], []
                            for f in bestOverallFeaturesFS:
                                arr1.append(rowI[f])
                                arr2.append(rowJ[f])
                            arr1.append(rowI[x])
                            arr2.append(rowJ[x])
                            if (smallestCurrDistanceFS > distance(arr1, arr2)): #if the existing smallest distance is greater than the distance between feature X at I and feature X at J
                                smallestCurrDistanceFS = distance(arr1, arr2)
                                rowOfBestDistanceFS = rowJ # the row at which it was founded at
                            #closing if
                        #closing if
                    #closing for
                    if (rowOfBestDistanceFS[0] == rowI[0]):
                        countForFS += 1
            #closing for
            #total number of times it was accurate for feature X
                kNNaccuracyFS = countForFS / len(newData) # 0.683333
                #print('This is kNN accuracy at', x, 'for Forward Selection:', kNNaccuracyFS)
                if (bestCurrAccuracyFS < kNNaccuracyFS):
                    bestCurrAccuracyFS = kNNaccuracyFS
                    bestCurrFeature = x

            # backward elimination

            countForBE = 0
            if (x in featuresInArray):
                for i in range(len(newData)): # validation row, value of newData is 300
                    rowI = newData[i] #ex: row 1
                    smallestCurrDistanceBE = 100
                    #biggestCurrDistance = 0
                    for j in range(len(newData)): #tests against everything except validation row, value of newData is 300
                        rowJ = newData[j] #ex: row 2
                        if (i != j): # if row 1 != row 2
                            arr3, arr4 = [], []
                            for q in featuresInArray:
                                arr3.append(rowI[q])
                                arr4.append(rowJ[q])
                            arr3.remove(rowI[x])
                            arr4.remove(rowJ[x])
                            if (smallestCurrDistanceBE > distance(arr3, arr4)): #if the existing smallest distance is greater than the distance between feature X at I and feature X at J
                                smallestCurrDistanceBE = distance(arr3, arr4)
                                rowOfBestDistanceBE = rowJ # the row at which it was founded at
                            #closing if
                        #closing if
                    #closing for
                    if (rowOfBestDistanceBE[0] == rowI[0]):
                        countForBE += 1
            #closing for
            #total number of times it was accurate for feature X
                kNNaccuracyBE = countForBE / len(newData) # 0.683333
                #print('This is kNN accuracy at', x, 'for Backward Elimination:', kNNaccuracyBE)
                if (bestCurrAccuracyBE < kNNaccuracyBE):
                    bestCurrAccuracyBE = kNNaccuracyBE
                    featureToRemove = x


        if (bestOverallAccuracyFS < bestCurrAccuracyFS):
            #print('Best overall accuracy is now', bestCurrAccuracy)
            bestOverallAccuracyFS = bestCurrAccuracyFS
            bestFeatures.append(bestCurrFeature)
        bestOverallFeaturesFS.append(bestCurrFeature)
        print('Best overall features for FS are: ', bestOverallFeaturesFS, 'with an accuracy of', bestCurrAccuracyFS)

        if (bestOverallAccuracyBE < bestCurrAccuracyBE):
            #print('Best overall accuracy is now', bestCurrAccuracyBE)
            bestOverallAccuracyBE = bestCurrAccuracyBE
            bestOverallFeaturesBE = featuresInArray
            #print('Best overall features: ', bestOverallFeaturesBE)
        featuresInArray.remove(featureToRemove)
        print('Features in the array for BE are now', featuresInArray, 'with an accuracy of', bestCurrAccuracyBE)
        #closing for
    #closing for

    print('Best overall features for FS is:', bestOverallFeaturesFS, 'with an accuracy of', bestOverallAccuracyFS)
    print('Best overall features for BE is:', bestOverallFeaturesBE, 'with an accuracy of', bestOverallAccuracyBE)

    i = 0

    biDirectionalArray = []
    for i in range(len(newData[0])):
        if (i in bestOverallFeaturesBE) and (i in bestOverallFeaturesFS):
            biDirectionalArray.append(i)


    print('The features that are important according to bi-direction are:', biDirectionalArray)
    return biDirectionalArray

### main UI of the code

if (val2 == '1'):
    forwardSelection(newData)
if (val2 == '2'):
    backwardElimination(newData)
if (val2 == '3'):
    biDirectional(newData)

print('Thank you for trying Geoffreys algorithm!')


"""sources used: 
https://www.guru99.com/reading-and-writing-files-in-python.html
https://www.youtube.com/watch?v=0aTtMJO-pE4
https://www.youtube.com/watch?v=R-ZMdOcZdXA
https://www.geeksforgeeks.org/bidirectional-search/
https://www.hackerearth.com/practice/python/getting-started/input-and-output/tutorial/
https://www.geeksforgeeks.org/taking-input-in-python/
slides from class

end of source"""
