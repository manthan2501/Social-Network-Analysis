# python program for network analysis

import snap 
Rnd = snap.TRnd(42) 
Rnd.Randomize()

import sys

file_name = "subgraphs/" + sys.argv[1] + ".txt"
G = snap.LoadEdgeList(snap.PUNGraph, file_name, 0, 1)

########

# number of nodes
j=0
for NI in G.Nodes():
     j = j+1

total_nodes = j
print("Number of nodes:",j)

# number of edges
j=0
for N in G.Edges():
  j = j+1

print("Number of edges:",j)

# number of nodes with degree = 7
j=0
for N in G.Nodes():
    if N.GetDeg() == 7:
      j = j+1

print("Number of nodes with degree=7:",j)

# Node id with highest nodes
m = 1
for N in G.Nodes():
  if N.GetInDeg() > m:
    m = N.GetInDeg()

for N in G.Nodes() :
  if N.GetInDeg() == m :
    print("Node id(s) with highest degree:",N.GetId())

# Plotting Degree distribution

import matplotlib.pyplot as plt

degs = []
val = []

for m in range(1, 70):
  j=0
  for N in G.Nodes() :
    if N.GetInDeg() == m :
      j = j+1
  degs.append(m)
  val.append(j)
  
plt.plot(degs, val)  
plt.xlabel(' Degrees ') 
plt.ylabel(' Nodes having x degree ')
plt.title(' Plot of the Degree distribution ')   
# plt.show()   ## uncomment this line to plot the graph

# approximate full diameter taking 10, 100, 1000 nodes and finding mean and variance

diam10 = snap.GetBfsFullDiam(G, 10)
print("Approximate full diameter by sampling 10 nodes:", diam10)

diam100 = snap.GetBfsFullDiam(G, 100)
print("Approximate full diameter by sampling 100 nodes:", diam100)

diam1000 = snap.GetBfsFullDiam(G, 1000)
print("Approximate full diameter by sampling 10000 nodes:", diam1000)

import numpy as np
a = np.array([diam10, diam100, diam1000])

print("Approximate full diameter (mean and variance):", round(np.mean(a),4), round(np.var(a),4) )

# approximate effective diameter taking 10, 100, 1000 nodes and finding mean and variance

NTestNodes = 10
IsDir = False
EffDiam10 = snap.GetBfsEffDiam( G, NTestNodes, IsDir)
print("Approximate effective diameter by sampling 10 nodes:", round(EffDiam10,4) )

NTestNodes = 100
IsDir = False
EffDiam100 = snap.GetBfsEffDiam( G, NTestNodes, IsDir)
print("Approximate effective diameter by sampling 100 nodes:", round(EffDiam100,4) )

NTestNodes = 1000
IsDir = False
EffDiam1000 = snap.GetBfsEffDiam( G, NTestNodes, IsDir)
print("Approximate effective diameter by sampling 1000 nodes:", round(EffDiam1000,4) )

import numpy as np
a = np.array([EffDiam10, EffDiam100, EffDiam1000])

print("Approximate effective diameter (mean and variance):", round(np.mean(a),4), round(np.var(a),4) )

# Plotting shortest path length distribution

nodes = []
diam = []
for m in range(1,1000, 100):
  nodes.append(m)
  diam.append(snap.GetBfsFullDiam(G, m))

plt.plot(nodes, diam)  
plt.xlabel(' Nodes ') 
plt.ylabel(' shortest path ')
plt.title(' Plot of the distribution of the shortest path lengths in the network ')   
#plt.show()   ## uncomment this line to show plot

# Fraction of nodes in biggest component

CntV = snap.TIntPrV()
snap.GetWccSzCnt(G, CntV)

for p in CntV:
    b = p.GetVal1()

print("Fraction of nodes in largest connected component:",  round( b/(total_nodes) ,4)  )    # b = 13971

# number of edge bridges

EdgeV = snap.TIntPrV()
snap.GetEdgeBridges(G, EdgeV)
j = 0
for edge in EdgeV:
    j = j+1

print("Number of edge bridges:",j)

# number of articulate points

ArtNIdV = snap.TIntV()
snap.GetArtPoints(G, ArtNIdV)

j=0
for NI in ArtNIdV:
    j = j+1

print("Number of articulation points:",j)

# Plotting Connected component distribution

sizes = []
counts = []
CntV = snap.TIntPrV()
snap.GetWccSzCnt(G, CntV)
for p in CntV:
    # print("size %d: count %d" % (p.GetVal1(), p.GetVal2()))
    sizes.append(p.GetVal1())
    counts.append(p.GetVal2())

plt.plot(sizes, counts)  
plt.xlabel(' size ') 
plt.ylabel(' count ')
plt.title(' Plot of the connected component ')   
# plt.show()   ## uncomment this line to show plot

# Average clustering coefficient
print("Average clustering coefficient:", round(snap.GetClustCf(G),4) )

# Number of triads
print("Number of triads:", snap.GetTriads(G) )

# Clustering coefficient of random node
N = G.GetRndNId(Rnd)
print("Clustering coefficient of random node %d: %d" % (N, round(snap.GetNodeClustCf(G, N),4) ) )   

# Number of triads random node participates
N = G.GetRndNId(Rnd)
print("Number of triads random node %d participates: %d" % (N, snap.GetNodeTriads(G, N)) )

# Number of edges that participate in at least one triad
NumTriadEdges = snap.GetTriadEdges(G)
print("Number of edges that participate in at least one triad:", NumTriadEdges)

# Plotting the clustering coefficient distribution

a=[0,0,0,0,0,0,0,0,0]
b=[0,1,2,3,4,5,6,7,8]

for N in G.Nodes():
  if snap.GetNodeClustCf(G, N.GetId()) > 0.8:
    a[8]=a[8]+1
  elif snap.GetNodeClustCf(G, N.GetId()) > 0.7:
    a[7]=a[7]+1
  elif snap.GetNodeClustCf(G, N.GetId()) > 0.6:
    a[6]=a[6]+1
  elif snap.GetNodeClustCf(G, N.GetId()) > 0.5:
    a[5]=a[5]+1
  elif snap.GetNodeClustCf(G, N.GetId()) > 0.4:
    a[4]=a[4]+1
  elif snap.GetNodeClustCf(G, N.GetId()) > 0.3:
    a[3]=a[3]+1
  elif snap.GetNodeClustCf(G, N.GetId()) > 0.2:
    a[2]=a[2]+1
  elif snap.GetNodeClustCf(G, N.GetId()) > 0.1:
    a[1]=a[1]+1
  else :
    a[0]=a[0]+1

plt.plot(b, a)  
plt.xlabel(' clustering coefficient ') 
plt.ylabel(' No. of Nodes ')
plt.title(' Plot of the clustering coefficient distribution ')   
# plt.show()  ## uncomment this line to show plots