#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  int maxA = 0;
  int maxO = 0;
  int maxX = 0;
  for(int i = 1; i<=n;i++){
      for(int j = i+1; j<=n;j++){
          if((i&j)>maxA && ((i&j)<k)){
              maxA = i&j;
          }
          if((i|j)>maxO && ((i|j)<k)){
              maxO = i|j;
          }
          if((i^j)>maxX && ((i^j)<k)){
              maxX = i^j;
          }
      }
  }
  printf("%d\n",maxA);
  printf("%d\n",maxO);
  printf("%d\n",maxX);
}

int main() {
    int n, k;

    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
