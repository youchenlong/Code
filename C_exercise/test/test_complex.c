#include"exercises/complex.h"

int main(){
    // 计算(8+6i)*(4+3i)/((8+6i)+(4+3i))
    // 计算(4+3i)*(-4-3i)/((4+3i)+(-4-3i))
    complex z1, z2, z3, z4, z;
    construct(&z1, 4, 3);
    construct(&z2, -4, -3);
    multiply(&z3, z1, z2);
    add(&z4, z1, z2);
    divide(&z, z3, z4);
    print_complex(z);
    return 0;
}