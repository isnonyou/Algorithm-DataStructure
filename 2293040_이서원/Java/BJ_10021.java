import java.util.Scanner;

class Main {  
  public static void main(String args[]) { 


    Scanner t = new Scanner(System.in);

    int l = t.nextInt();

    for (int i = 0; i < l; i++) {

      int a = t.nextInt();
      int b = t.nextInt();

      System.out.println("Case #"+(i+1)+": "+(a+b));

    }
    
  } 
}