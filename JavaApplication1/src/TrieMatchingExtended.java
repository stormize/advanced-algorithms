import java.io.*;
import java.util.*;

class Node
{
	public static final int Letters =  4;
	public static final int NA      = -1;
	public int next [];
	public boolean patternEnd;

	Node ()
	{
		next = new int [Letters];
		Arrays.fill (next, NA);
		patternEnd = false;
	}
}

public class TrieMatchingExtended implements Runnable {
	int letterToIndex (char letter)
	{
		switch (letter)
		{
			case 'A': return 0;
			case 'C': return 1;
			case 'G': return 2;
			case 'T': return 3;
			default: assert (false); return Node.NA;
		}
	}
        char indexToLetter(int index) {
        switch (index) {
            case 0:
                return 'A';
            case 1:
                return 'C';
            case 2:
                return 'G';
            case 3:
                return 'T';
            default:
                assert (false);
                return '?';
        }
    }

	List <Integer> solve (String text, int n, List <String> patterns) {
		List <Integer> result = new ArrayList <Integer> ();
                  List<Node> trie =  build(patterns);
                  int k=0;
                  Node root=trie.get(0);
                  while(!text.isEmpty()){
                      int match=-1;
                      char currentSymbol=text.charAt(0);
                      Node currentNode=root;
                      int l=0;
                      while(true){
                          if(currentNode.patternEnd){
                              match=k;
                              break;
                          } else if(currentNode.next[letterToIndex(currentSymbol)]!=Node.NA){
                          currentNode=trie.get(currentNode.next[letterToIndex(currentSymbol)]);
                          if(l+1 < text.length()){
                              currentSymbol=text.charAt(++l);
                          } else{
                              if(currentNode.patternEnd){
                                  match=k;
                              }
                              break;
                          }
                      }else{
                              break;
                          }
                      }
                      if(match!=-1){
                          result.add(match);
                      }
                      k++;
                      text=text.substring(1);
                  }
                  
                
		// write your code here

		return result;
	}
      List<Node> build(List<String> patterns){
          List<Node> trie =new ArrayList<>();
          trie.add(new Node());
          for(String pattern: patterns){
              int currentNodeIndex=0;
              
              for(int i=0; i<pattern.length();i++){
                  char currentSymbol=pattern.charAt(i);
                  Node currentNode=trie.get(currentNodeIndex);
                  int currentSymbolIndex=letterToIndex(currentSymbol);
                  if(currentNode.next[currentSymbolIndex]==Node.NA){
                      Node newNode = new Node();
                      trie.add(newNode);
                      int newNodeIndex=trie.size()-1;
                      currentNode.next[currentSymbolIndex]=newNodeIndex;
                      currentNodeIndex=newNodeIndex;   
                  }
                  else{
                      currentNodeIndex=currentNode.next[currentSymbolIndex];
                  }
                  if(i ==pattern.length()-1){
                      Node endNode =trie.get(currentNodeIndex);
                        endNode.patternEnd=true;
                  }
              }
          }
          return trie;
      }
	public void run () {
		try {
			BufferedReader in = new BufferedReader (new InputStreamReader (System.in));
			String text = in.readLine ();
		 	int n = Integer.parseInt (in.readLine ());
		 	List <String> patterns = new ArrayList <String> ();
			for (int i = 0; i < n; i++) {
				patterns.add (in.readLine ());
			}

			List <Integer> ans = solve (text, n, patterns);

			for (int j = 0; j < ans.size (); j++) {
				System.out.print ("" + ans.get (j));
				System.out.print (j + 1 < ans.size () ? " " : "\n");
			}
		}
		catch (Throwable e) {
			e.printStackTrace ();
			System.exit (1);
		}
	}

	public static void main (String [] args) {
		new Thread (new TrieMatchingExtended ()).start ();
	}
}
