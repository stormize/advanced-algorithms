class Trie(object):
    def __init__(self):
        self.children={}
        self.indexes=[]
class prefix_trie(object):
    def __init__(self):
        self.root=Trie()
    def add_prefix(self,str,index):
        for i in range(len(str)):
            rev=str[:i][::-1]
            node = self.root
            for char in rev:
                if char not in node.children:
                    node.children[char] = Trie()
                node = node.children[char]
            node.indexes.append(index)
    def match(self):
        l=0
        node =self.root
        adj=[]

