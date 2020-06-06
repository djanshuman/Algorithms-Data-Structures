//Java Palindrome
package handson;

public class PalindromeCheck {
	
	public boolean Palin(String str,int str1,int last) {
		
		if(str1==last || str1 > last){
			return true;
		}
		if(str.charAt(str1)!=str.charAt(last)) {
			return false;
		}
		return Palin(str,str1+1,last-1);
			
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		PalindromeCheck obj= new PalindromeCheck();
		String test="NOOn";
		System.out.println(obj.Palin(test.toLowerCase(),0, test.length()-1));

	}
}
