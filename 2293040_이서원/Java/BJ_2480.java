import java.util.Scanner;

class Main {  
  public static void main(String args[]) { 


    Scanner t = new Scanner(System.in);

    int a = t.nextInt();
    int b = t.nextInt();
    int c = t.nextInt();

    if (a == b && b == c) {
      System.out.println(10000+a*1000);
    }

    else if (a == b || a == c) {
      System.out.println(1000+a*100);
    }

    else if (b == c) {
      System.out.println(1000+b*100);
    }

    else if (Math.max(a,b) == a){
      System.out.println(Math.max(a,c)*100);
    }

    else {
      System.out.println(Math.max(b,c)*100);
    }
    
  } 
}