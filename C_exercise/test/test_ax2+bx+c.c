#include"exercises/ax2+bx+c.h"

int main(){
    float *result = solve(1, 3, 2);
    printf("%.2f %.2f", result[0], result[1]);
    return 0;
}