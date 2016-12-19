import argparse
import random

#default name of output files
NODESFILE = "nodes.csv"
EDGESFILE = "edges.csv"

#data entry restriction functions
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
parser.add_argument('--output-files', '-of',
                    type=str,
                    nargs=2,
                    default=[NODESFILE,EDGESFILE],
                    help='output names file "1st nodesFile.csv 2nd edgesFile.csv"')
args = parser.parse_args()

nodesList = []
edgesList = []

for i in range(args.nodes):
    nodesList.append(i)
    for j in range(i+1, args.nodes):
        #random int between 0 <= x <= 10;
        if args.probability > 0 and random.random() <= args.probability:
            edgesList.append([i,j])

# Write Nodes File
nodesFile = open(args.output_files[0], 'w')
nodesFile.write("Id\n")
for i in nodesList:
    nodesFile.write(str(i)+'\n')
nodesFile.close()

#Write Edges File
edgesFile = open(args.output_files[1], 'w')
edgesFile.write("Source;Target;Type\n")
for i in edgesList:
    edgesFile.write(str(i[0]) + ";")
    edgesFile.write(str(i[1]) + ";")
    edgesFile.write("Undirected\n")
edgesFile.close()
