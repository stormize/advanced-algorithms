/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package suffixarray;

/**
 *
 * @author amrma
 */
public class SuffixArray {

    public static int[] sortChars(String s){
        char[] S=s.toCharArray();
        System.out.println(S.length);
        int[] count=new int[26];
        int[] order = new int[S.length];
        for (int i =0;i<=s.length()-1;i++){
            count[(int)S[i]%26]=count[(int)S[i]%26]+1;
        }
        for(int i =1;i<count.length-1;i++){
            count[i]=count[i]+count[i-1];
        }
        for (int i=S.length-1;i<=0;i--){
            int c =(int) S[i];
            count[c]=count[c]-1;
            order[count[c]]=i;
            System.out.println(i);
        }
        return order;
    }
    public static void main(String[] args) {
       
        
       
    }
    
}
