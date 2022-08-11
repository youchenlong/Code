#include"../exercises/matrix.h"

int main(){
    // 乘法
    // matrix A, B;
    // create(&A, 2, 3);
    // create(&B, 3, 2);
    // init_matrix(&A);
    // init_matrix(&B);
    // matrix result = multiply(A, B);

    // 加法
    // matrix A, B;
    // create(&A, 2, 2);
    // create(&B, 2, 2);
    // init_matrix(&A);
    // init_matrix(&B);
    // matrix result = add(A, B);

    // 减法
    // matrix A, B;
    // create(&A, 2, 2);
    // create(&B, 2, 2);
    // init_matrix(&A);
    // init_matrix(&B);
    // matrix result = sub(A, B);

    // 行阶梯形
    // matrix A;
    // create(&A, 3, 4);
    // init_matrix(&A);
    // row_echelon(&A);

    // 矩阵的秩
    // matrix A;
    // create(&A, 3, 4);
    // init_matrix(&A);
    // int r = rank(A);
    // printf("the rank of matrix is %d", r);

    // 矩阵的行列式
    // matrix A;
    // create(&A, 3, 3);
    // init_matrix(&A);
    // float res = det(A);
    // printf("the determinant of the matrix is %f", res);

    // 代数余子式
    // matrix A;
    // create(&A, 4, 4);
    // init_matrix(&A);
    // // float res = confactor(A, 0, 0);
    // float res = algebraic_confactor(A, 1, 1);
    // printf("the factor of the matrix(determinant) is %f", res);

    // 逆矩阵
    // matrix A;
    // create(&A, 3, 3);
    // init_matrix(&A);
    // matrix inv = inverse(A);
    // print_matrix(inv);

    // 矩阵的行阶梯型
    matrix A;
    create(&A, 3, 4);
    init_matrix(&A);
    row_echelon(&A);
    print_matrix(A);

    // 矩阵的列阶梯型
    // matrix A;
    // create(&A, 4, 4);
    // init_matrix(&A);
    // col_echelon(&A);
    // print_matrix(A);

    return 0;
}