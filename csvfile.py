import csv
import pprint
from difflib import SequenceMatcher

# http://python-cluster.sourceforge.net/
from cluster import HierarchicalClustering

s=[]
with open("db.csv") as a:
    rows=csv.reader(a)
    for row in rows:
        
        s.append(row[1])
y=s[1:50]
def distance(url1, url2):
    ratio = SequenceMatcher(None, url1, url2).ratio()
    return 1.0 - ratio
# Perform clustering
hc = HierarchicalClustering(y, distance)
clusters = hc.getlevel(0.2)

pprint.pprint(clusters)
