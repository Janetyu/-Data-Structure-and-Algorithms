package lanqiaobei.enerty;

import java.util.Scanner;

/**
 * ���г�ʱ
 * @author ASUS
 *
 */
public class Fibonacci_1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println(Fibo(n)%10007);
	}
	
	public static int Fibo(int n){
		if(n == 1 || n == 2){
			return 1;
		}else{
			return Fibo(n-1)+Fibo(n-2);
		}
	}
}
