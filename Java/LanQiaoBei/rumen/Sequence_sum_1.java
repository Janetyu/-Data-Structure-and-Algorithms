package lanqiaobei.enerty;

import java.util.Scanner;

public class Sequence_sum_1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
//		long temp = 0;
		Long num1 = sc.nextLong();
		//‘À––≥¨ ±
//		for(long i = 1; i <= num1; i++){
//			temp += i;
//		}
		
		long temp = (num1*(num1+1))/2;
		System.out.println(temp);
		
	}
}
