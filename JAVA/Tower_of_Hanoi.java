package handson;

public class TOH {
	
	public void hanoi(int n,char A, char B,char C) {
		
		//System.out.println(n +"-"+A+"-"+B+"-"+C);
		
		if(n==1) {
			System.out.println("Move "+ n+" Disc " + "from "+ A+"Tower" +"-"+ C+"TOWER");
		}
		else {
					
			hanoi(n-1,A,C,B);
			System.out.println("Move "+ n+" Disc " + "from "+ A+"Tower" +"-"+ C+"TOWER");
			hanoi(n-1,B,A,C);
			
		}
		
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		TOH obj= new TOH();
		obj.hanoi(2, 'A' ,'B', 'C');
	}

}
