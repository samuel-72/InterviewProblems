import java.util.Scanner;

public class computeNxNPaths {

	int n;
	long path; // I am leaving this to be a long datatype as this solution does not scale well for N > 16
	
	public computeNxNPaths(int n, long path)
	{
		this.n = n;
		this.path = path;
	}
	
	public Boolean recursiveTraversal(int row,int col)
	{
		if ( row == this.n || col == this.n )
		{
			this.path += 1L;
			return true;
		}
		if ( row > this.n || col > this.n )
		{
			return false;
		}
		
	    recursiveTraversal(row+1,col);
	    recursiveTraversal(row,col+1);
		return false;
	}
	
	public static void main(String[] args) {
		
		int N = 0;
		Scanner sc = new Scanner(System.in);
		System.out.println("This program computes the number of distinct paths in a NxN matrix.\n");
		System.out.println("Please enter the value of N :");
		try
		{
			N = sc.nextInt();
		}
		catch(Exception e)
		{
			System.out.println("\nThe input you entered resulted in the error below." + e + "\n\nPlease enter a valid input. Valid input is any integer greater than or equal to 0");
			System.exit(-1);
		}
		sc.close();
		if (N < 0)
		{
			System.out.println("Please enter a value greater than or equal to 0.");
			System.exit(0);
		}
		else if (N == 0)
		{
			System.out.println("\nTotal no of paths : " + 1);
			System.exit(0);
		}
		else if ( N == 1)
		{
			System.out.println("\nTotal no of paths : " + 2);
			System.exit(0);
		}
		else
		{
			try
			{
				computeNxNDP totalPaths = new computeNxNDP(N);
				System.out.println("\nTotal no of paths : " + (totalPaths.recursiveTraversal(N, N))  + "\n");
				System.exit(0);
			}
			catch(Exception err)
			{
				System.out.println("\nFor the given N, we have hit an exception.\n" + err);
				System.exit(-1);
			}
		}
	}
	
}
