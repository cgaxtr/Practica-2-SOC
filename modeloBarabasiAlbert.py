import argparse
import random
import collections

#anadir al parseo la opcion de ficheros de salida

def restricted_positive(x):
    x = int(x)
    if x < 1:
        raise argparse.ArgumentTypeError('%s must be positive'%(x))
    return x

parser = argparse.ArgumentParser(usage='%(prog)s [options]')
parser.add_argument('--links', '-m',
                    type=restricted_positive,
                    help='number of edges to links new nodes',
                    required=True)
parser.add_argument('--time', '-t',
                    type=restricted_positive,
                    help='number of execution steps',
                    required=True)
args = parser.parse_args()

edgeList = [] #edges are defined such as vector[origin,destination]
nodesDict = {} #key = id node, value = grade of node
totalGrade = 0 #contains the sum of grades of all nodes


#complete graph with the initial nodes
for i in range(args.links + 1):
    if not nodesDict.has_key(i):
        nodesDict[i]=0
    for j in range(i+1, args.links + 1):
        if not nodesDict.has_key(j):
            nodesDict[j]=0
        edgeList.append([i,j])
        nodesDict[i] = nodesDict.get(i) + 1
        nodesDict[j] = nodesDict.get(j) + 1
        totalGrade += 2
#debug
print "<-----------INICIO----------->"
print nodesDict
print edgeList

#execute steps
for i in range(args.time):
    nodesLinked = [] #Nodes that have been linked

    newNode = len(nodesDict) #new node id
    nodesDict[newNode] = 0 #adding new node
    
    #debug
    print "<-----------ITER" + str(i) + "----------->"
    
    while(len(nodesLinked) < args.links):
        randomInt = random.randint(0,totalGrade-1)
        print "randomInt" + str(randomInt)
        key = 1; #key to dict access
        probabilityAcumulated = nodesDict.get(0)
        while probabilityAcumulated < randomInt:
            probabilityAcumulated += nodesDict.get(key)
            key += 1
        if not key-1 in nodesLinked:
            edgeList.append([newNode,key-1])
            nodesLinked.append(key-1)
            nodesDict[newNode] = nodesDict.get(newNode) + 1
            nodesDict[key-1] = nodesDict.get(key-1) + 1

    totalGrade += args.links*2

    #debug
    print nodesDict
    print edgeList
# save data
