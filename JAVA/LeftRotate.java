package handson;

public class LeftRotate {
	
	public void Rotate(int []arr1,int n) {
		
		int temp= arr1[0];
		
		for (int i=1;i<n;i++) { 
			arr1[i-1]=arr1[i];
		}
		arr1[n-1]=temp;
		
		for(int i=0;i<n;i++) {
			System.out.println(arr1[i]);
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int arr1[]= {90,20,49,10,89};
		LeftRotate rotate= new LeftRotate();
		rotate.Rotate(arr1, 5);
	}
}
