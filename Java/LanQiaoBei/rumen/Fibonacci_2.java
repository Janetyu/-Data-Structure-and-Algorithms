package lanqiaobei.enerty;

import java.util.Scanner;

public class Fibonacci_2 {
	public static void main(String[] args) {
		int a = 1,b = 1,temp = 1;
		int fornum = 10007;
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for(int i = 3; i <= n; i++){
			temp = (a + b)%fornum;
			a = b;
			b = temp;
		}		
		System.out.println(temp);
	}
	
//	public static int Fibo(int n){
//		if(n == 1 || n == 2){
//			return 1;
//		}else{
//			return Fibo(n-1)+Fibo(n-2);
//		}
//	}
}
