import argparse
import random

#anadir al parseo la opcion de ficheros de salida

NODESFILE = "nodes.csv"
EDGESFILE = "edges.csv"

def restricted_float(x):
    x = float(x)
    if x < 0.0 or x > 1.0:
        raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]"%(x))
    return x

def restricted_positive(x):
    x = int(x)
    if x < 1:
        raise argparse.ArgumentTypeError('%r must be positive'%(x))
    return x

parser = argparse.ArgumentParser(usage='%(prog)s [options]')

parser.add_argument('--nodes', '-n',
                    type=restricted_positive,
                    help='number of nodes to generate random networks',
                    required=True)
parser.add_argument('--probability','-p',
                    type=restricted_float,
                    help='probability to generate edge',
                    required=True)
args = parser.parse_args()

listNodes = []
listAristas = []

for i in range(args.nodes):
    listNodes.append(i)
    for j in range(i+1, args.nodes):
        #random int between 0 <= x <= 10;
        if args.probability*10 > 0 and random.randint(0,10) <= args.probability
            listAristas.append([i,j])

    # Write Nodes File
    nodesFile = open(NODESFILE, 'w')
    nodesFile.write("Id\n")
    for i in listNodes:
        nodesFile.write(str(i)+'\n')
    nodesFile.close()

    #Write Edges Nodes File
    edgesFile = open(EDGESFILE, 'w')
    edgesFile.write("Source;Target;Type\n")
    for i in listAristas:
        edgesFile.write(str(i[0]) + ";")
        edgesFile.write(str(i[1]) + ";")
        edgesFile.write("Undirected\n")

    edgesFile.close()
