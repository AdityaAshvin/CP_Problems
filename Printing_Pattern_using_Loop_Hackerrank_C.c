#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    int len = 2*n-1;
    int minV,minH,minD;
    for (int i=1; i <=len; i++) {
      for (int j=1; j<=len; j++) {
        minV = i<=len-i ? i -1: len-i;
        minH = j<=len-j ? j -1: len-j;
        minD = minV<=minH ? minV : minH;
        printf("%d ",n-minD);
      }
      printf("\n");
  }
return 0;
}