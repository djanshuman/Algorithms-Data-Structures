package handson;

public class SumDigits {

	public int Sum(int n,int accum,int last_digit) {
		
		if(n<1) {
			return accum+last_digit;
		}
		int x=n/10;
		int y=x%10;
		//System.out.println(x +","+ y);
		return Sum(x,accum+y,last_digit);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SumDigits obj= new SumDigits();
		int num=9987;
		System.out.println(obj.Sum(num,0,num%10));
	}

}
