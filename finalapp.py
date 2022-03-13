import csv
import json
import pandas as pd

try:
    df = pd.read_csv (r'C:\Users\91797\OneDrive\Desktop\akshata\data.csv')
    len=len(df.columns)
except IOError:
    print("File not accessible")

class Node(object):

    def __init__(self, name, id=None,url=None):
        self.name = name
        self.children = []
        self.url = url
        self.id = id

    def child(self, cnam,cid, curl):
        child_found = [c for c in self.children if c.id == cid]
        if not child_found:
            _child = Node(cnam,cid, curl)
            self.children.append(_child)
        else:
            _child = child_found[0]
        return _child

    def as_dict(self):
        res = {'label': self.name}
        res['id']=self.id
        res['link'] = self.url

        if self.name:
            res['children'] = [c.as_dict() for c in self.children]
        return res

# root = Node('Base URL',00000,'https://groceries.dmart.com/browse')
try:
    with open(r'C:\Users\91797\OneDrive\Desktop\akshata\data.csv') as f:
        reader = csv.reader(f)
        next=root
        for row in reader:
            q=3
            m=row
            next=root.child(m[1],m[2],m[3])
            while q<len-1:
                next=next.child(m[q+1],m[q+2],m[q+3])
                q=q+3
    print(json.dumps(root.as_dict(), indent=4))
except IOError:
    print("File not accessible")

# with open(r'D:\PythonVSCode\test\data.csv') as f:
#     reader = csv.reader(f)
#     q=0
#     for row in reader:
#         m=row
#         print(m)
#         root.child(m[1],m[2],m[3]).child(m[4],m[5],m[6]).child(m[7],m[8],m[9])

