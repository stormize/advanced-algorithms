
package trie;

import java.util.HashMap;
import java.util.Scanner;


public class Trie {
public static class Node{
HashMap<Character,Node> children=new HashMap();
char value;
boolean isLeaf;
Node(char value){
    this.value=value;
}
Node(){    
}
}
public static class myTrie{
     int numb=0;
    private Node root;
  myTrie(){
      root = new Node();
  }
  void insert(String word){
    Node currentNode=root;
    for(int i  =0 ; i <word.length() ;i++){
        char currentSymbol = word.charAt(i);
        if(currentNode.children.containsKey(currentSymbol)){
        currentNode=currentNode.children.get(currentSymbol);
        }
        else{
           currentNode.children.put(currentSymbol, new Node(currentSymbol));
           currentNode=currentNode.children.get(currentSymbol);
        }
        if(i==word.length()-1)
            currentNode.isLeaf=true;
    }
  }
  public int search(String text){
      int count=0;
         Node currentNode = root;
         for(int i =0 ; i < text.length();i++){
             char currentSymbol=text.charAt(i);
             if(currentNode.children.containsKey(currentSymbol)){
                 count +=currentNode.children.size()-1;
             currentNode=currentNode.children.get(currentSymbol);
             }
             else{return 0;}
            
         }
         
         int result=count(currentNode);
         numb=0;
          return result; 
          
  }
  public int count(Node current){
     
     for(Node node :current.children.values()){
         
        count(node);
         
     }
      if(current.isLeaf){
         numb++;
      }
      
      return numb;
  }
 
}
 
    public static void main(String[] args) {
        myTrie tree = new myTrie();
  tree.insert("shid");
  System.out.println(tree.search("shid"));
         
    }
    
}
