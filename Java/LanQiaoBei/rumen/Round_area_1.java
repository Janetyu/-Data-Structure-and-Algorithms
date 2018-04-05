package lanqiaobei.enerty;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Round_area_1 {
	public static void main(String[] args) {
		double PI=3.14159265358979323;
		//double PI= Math.atan(1.0)*4;
		Scanner sc = new Scanner(System.in);
		int r = sc.nextInt();
		double s = PI * r *r;
		DecimalFormat df = new DecimalFormat("#.0000000");
		System.out.println(df.format(s));
	}
}
