package handson;

public class Reverse {
	
	public void rev(int arr1[], int n) {
		
		int low=0;
		int high=n-1;
		while(low <=high) {
			int temp=arr1[low];
			arr1[low]=arr1[high];
			arr1[high]=temp;
			low++;
			high--;
		}
		
		for (int i=0;i<n;i++) {
			System.out.println(arr1[i]);
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int arr1[]= {90,20,49,10,89};
		Reverse rev1= new Reverse();
		rev1.rev(arr1, 5);
	}

}
