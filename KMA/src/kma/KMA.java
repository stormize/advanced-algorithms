/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package kma;

import java.util.ArrayList;

/**
 *
 * @author amrma
 */
public class KMA {

    /**
     * @param args the command line arguments
     */
    static int[] prefix(String[] s){
        int [] result= new int[s.length];
        int border=0;
        result[0]=0;
        for(int i =1;i<s.length;i++){
            while(border >0 && !s[border].equals(s[i])){
            border=result[border-1];
            }
            if(s[i].equals(s[border]))
                border++;
            else
                border=0;
           result[i]=border;             
        }
        return result;
    }
   static ArrayList<Integer> KMP(String str,String pat){
       String[] s=str.split("");
       String[] p=pat.split("");
       int [] prefix=prefix(p);
        ArrayList<Integer> result=new ArrayList<Integer>();
        for(int i=0,k=0;i<s.length;i++){
            while(k>0 &&!p[k].equals(s[i])){
                k=prefix[k-1];
            }
            if(p[k].equals(s[i]))
                k++;
            if(k==p.length){
                result.add(i-p.length+1);
                k=prefix[k-1];
            }
        }
        return result;
    }
    public static void main(String[] args) {
       for(int x: KMP("stringtr","r")){
           System.out.println(x);
       }
       
     
    }
    
}
