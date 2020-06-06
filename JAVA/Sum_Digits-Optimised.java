package handson;

public class Sum_Digits {

	public int Sum(int n) {
		
		//System.out.println(n);
		
		if(n<1) {
			return n;
		}
		return Sum(n/10) + n%10;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Sum_Digits obj= new Sum_Digits();
		int num=9987;
		System.out.println(obj.Sum(num));
	}

}
