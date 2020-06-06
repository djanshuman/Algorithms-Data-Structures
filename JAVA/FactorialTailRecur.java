package handson;

public class FactorialTailRecur {
	
	public int Facto(int n,int accum) {
	
		if(n<1) {
			return accum;
		}
		else {
		return Facto(n-1,n*accum);
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		FactorialTailRecur obj= new FactorialTailRecur();
		System.out.println((obj.Facto(5, 1)));
		
	}

}
