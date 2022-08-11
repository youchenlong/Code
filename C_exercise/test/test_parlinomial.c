#include"exercises/parlinomial.h"

int main(){
    // 初始化两个多项式
    AList p1;
    AList p2;
    p1 = create(4);
    p2 = create(3);
    DataType d1[4] = {{7, 0}, {3, 1}, {9, 8}, {5, 17}};
    DataType d2[3] = {{8, 1}, {22, 7}, {9, 8}};
    for(int k = 0; k < 4; k++){
        append(&p1, d1[k]);
    }
    for(int k = 0; k < 3; k++){
        append(&p2, d2[k]);
    }
    // 两个多项式相加
    AList result;
    result = add(p1, p2);
    // 输出结果
    traverse(result);
    return 0;
}