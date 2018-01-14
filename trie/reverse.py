class Node :
 value=''
 endWord=False
 children=dict()
 def __init__(self,string):
  self.value=string

class trie:
 root=Node("%")
 def add_string(self,string):
  current_node=self.root
  for i in string:
     if i == string[len(string)-1]:
         current_node.endWord=True
     if i in current_node.children:
      current_node = current_node.children.get(i)
     else:
      current_node.children[i]=Node(i)
      current_node = current_node.children.get(i)
  print(self.root.children.get('m').children)

 def find_string(self,string):
      current_node =self.root
      for i in string:
          if i == string[len(string)-1] and current_node.children.__len__()<1:

              return False
          if i in current_node.children:

              current_node = current_node.children.get(i)


          else:
              return False
          print(current_node.children.keys())
      return True


tree = trie()
tree.add_string("amr")


