import java.util.*;

public class computeNxNDP {

	int n;
	double pathSeen[][];
	
	public computeNxNDP(int n)
	{
		this.n = n;
		pathSeen = new double[n+1][n+1];
		for (int i=0;i<=this.n;i++)
		{
			this.pathSeen[i][0] = 1.0;
			this.pathSeen[0][i] = 1.0;
		}
	}
	
	public double recursiveTraversal(int row,int col)
	{
		if ( row < 0 || col < 0 )
		{
			return 0;
		}
		
		if ( this.pathSeen[row][col] > 0 )
		{
			return this.pathSeen[row][col];
		}
		else
		{
			this.pathSeen[row][col] = recursiveTraversal(row-1,col) + recursiveTraversal(row,col-1); 
			return this.pathSeen[row][col];
		}
		
	}
	
	public static void main(String[] args) {
		
		int N=0;
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
