import java.io.*;
import java.util.*;

public class Solution {
    public static void insertionSort(int[] arr,int n){
        for (int j = 1; j < n; j++) {  
            int key = arr[j];  
            int i = j-1;  
            while ( (i > -1) && ( arr [i] > key ) ) {  
                arr[i+1] = arr [i];  
                i--;  
            }  
            arr[i+1] = key;  
        }      
    }
    
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++)
            arr[i]=sc.nextInt();
        insertionSort(arr,n);
        for(int i=0;i<n;i++){
            System.out.print(arr[i]+" ");
            
        }
    }
}
