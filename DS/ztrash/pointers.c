// // #include<stdio.h>
// // int main(int argc, char const *argv[])
// // {
// //     int a[5]={1,2};
// //     int *ptr;

// //     for (int i = 0; i < 2; i++)
// // {
// // scanf("%d",&i[a]);
// // }


// //     return 0;
// // }






// // PROGRAM FOR POINTER TO POINTER

// #include<stdio.h>
// #include<conio.h>


// int main()
// {
// 	int m[3][3] = {
// 					{1,2,3},
// 					{4,5,6},
// 					{7,8,9}
// 				};

// 	int i,j;

// 	for(i= 0; i<3;i++)
// 	{
// 		//putch('\n'); // Error
// 		putchar('\n');

// 		for(j= 0; j<3;j++)
// 		{
// 			// printf("\t%d",m[i][j]);
// 			// printf("\t%d",*(m[i]+j));
// 			printf("\t%d",*(*(m+i)+j));
// 			// assume i = 1, j = 2
// 		}
// 	}
// 	return 0;
// }



// PROGRAM FOR POINTER TO POINTER
#include<stdio.h>
#include<conio.h>

int main()
{
	char *days[7] = {
						"Sunday",
						"Monday",
						"Tuesday",
						"Wednesday",
						"Thursday",
						"Friday",
						"Saturday"
					};
	int i;

	for(i=0; i<7;i++)
	{
		// printf("\n%s",days[i]);
		printf("\n%u",&days[i]);
	}
    return 0;
}