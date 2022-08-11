#include<stdlib.h>
#include<stdio.h>
#include<math.h>

typedef struct{
    int row;            // 行
    int col;            // 列
    float **matrix;     // 元素
}matrix;

void create(matrix *m, int row, int col);                       // 创建
void init_matrix(matrix *m);                                    // 初始化
matrix add(matrix A, matrix B);                                 // 加法
matrix sub(matrix A, matrix B);                                 // 减法
matrix multiply(matrix A, matrix B);                            // 乘法
void transpose(matrix *m);                                      // 转置
void row_trans_swap(matrix *m, int i, int j);                   // 交换两行(行和列从0开始)
void row_trans_sub(matrix *m, int i, int j, float multiple);    // 两行相减(第i行减去第j行的multiple倍)
void row_echelon(matrix *m);                                    // 将矩阵转换为行阶梯型
void col_trans_swap(matrix *m, int i, int j);                   // 交换两列(行和列从0开始)
void col_trans_sub(matrix *m, int i, int j, float multiple);    // 两列相减(第i列减去第j列的mutliple倍)
void col_echelon(matrix *m);                                    // 将矩阵转换为列阶梯型
int rank(matrix m);                                             // 求矩阵的秩
int inversion_number(int array[], int N);                       // 逆序数
float det(matrix m);                                            // 计算方阵的行列式
float confactor(matrix m, int i, int j);                        // 求余子式(行和列从0开始)
float algebraic_confactor(matrix m, int i, int j);              // 求代数余子式(行和列从0开始)
matrix inverse(matrix m);                                       // 求逆矩阵
void print_matrix(matrix m);                                    // 输出


void create(matrix *m, int row, int col){   
    // 声明一个矩阵
    m->row = row;
    m->col = col;
    m->matrix = (float **)malloc(sizeof(float *)*m->row);
    for(int i = 0; i < m->row; i++){
        m->matrix[i] = (float *)malloc(sizeof(float)*m->col);
    }  
    for(int i = 0; i < m->row; i++){
        for(int j = 0; j < m->col; j++){
            // 初始化为0
            m->matrix[i][j] = 0;
        }
    }  
}

void init_matrix(matrix *m){
    // 初始化矩阵
    printf("matrix(%d, %d)  input element:\n", m->row, m->col);
    for(int i = 0; i < m->row; i++){
        for(int j = 0; j < m->col; j++){
            scanf("%f", &m->matrix[i][j]);
        }
    } 
}

matrix add(matrix A, matrix B){
    // 判断矩阵A和矩阵B是否为同型矩阵
    if(A.row != B.row || A.col != B.col){
        printf("size error, matrix A's column(row) doesn't equal to matrix B's column(row)");
        exit(0);
    }
    // 计算结果并返回
    matrix result;
    create(&result, A.row, A.col);
    for(int i = 0; i < result.row; i++){
        for(int j = 0; j < result.col; j++){
            result.matrix[i][j] += A.matrix[i][j] + B.matrix[i][j]; 
        }
    }
    return result;
}

matrix sub(matrix A, matrix B){
    // 判断矩阵A和矩阵B是否为同型矩阵
    if(A.row != B.row || A.col != B.col){
        printf("size error, matrix A's column(row) doesn't equal to matrix B's column(row)");
        exit(0);
    }
    // 计算结果并返回
    matrix result;
    create(&result, A.row, A.col);
    for(int i = 0; i < result.row; i++){
        for(int j = 0; j < result.col; j++){
            result.matrix[i][j] += A.matrix[i][j] - B.matrix[i][j]; 
        }
    }
    return result;
}

matrix multiply(matrix A, matrix B){
    // 判断矩阵A的行与矩阵B的列是否相等
    if(A.col != B.row){
        printf("size error, matrix A's column doesn't equal to matrix B's row");
        exit(0);
    }
    // 计算结果并返回
    matrix result;
    create(&result, A.row, B.col);
    for(int i = 0; i < result.row; i++){
        for(int j = 0; j < result.col; j++){
            for(int k = 0; k < A.col; k++){
                result.matrix[i][j] += A.matrix[i][k] * B.matrix[k][j];
            }
        }
    }
    return result;
}

void transpose(matrix *m){
    // 转置
    matrix temp = *m;
    create(m, m->col, m->row);
    for(int i = 0; i < m->row; i++){
        for(int j = 0; j < m->col; j++){
            m->matrix[i][j] = temp.matrix[j][i];
        }
    }
}

void row_trans_swap(matrix *m, int i, int j){
    // 交换两行
    float temp;
    for(int k = 0; k < m->col; k++){
        temp = m->matrix[i][k];
        m->matrix[i][k] = m->matrix[j][k];
        m->matrix[j][k] = temp;
    }
}

void row_trans_sub(matrix *m, int i, int j, float multiple){
    // 两行相减
    for(int k = 0; k < m->col; k++){
        m->matrix[i][k] -= m->matrix[j][k] * multiple;
        if(fabs(m->matrix[i][k]) < __FLT_EPSILON__){
            m->matrix[i][k] = 0;
        }
    }
}

void row_echelon(matrix *m){
    int i = 0;
    int j = 0;
    // if(m->row < m->col){
    //     transpose(m);
    // }
    while(i < m->row && j < m->col){
        // 情形1：如果matrix[i][j]不为0
        if(m->matrix[i][j] != 0){
            // 首元素置1
            float divisor = m->matrix[i][j];
            for(int k = j; k < m->col; k++){
                m->matrix[i][k] /= divisor;
                if(fabs(m->matrix[i][k]) < __FLT_EPSILON__){
                    m->matrix[i][k] = 0;
                }
            }
            // 同一列下方元素置0
            for(int k = i + 1; k < m->row; k++){
                row_trans_sub(m, k, i, m->matrix[k][j]);
            }
            i++;
            j++;
        }
        // 情形2：如果matrix[i][j]为0
        else{
            // 向下寻找matrix[k][j]不为0的行
            int k;
            for(k = i + 1; k < m->row; k++){
                if(m->matrix[k][j] != 0){
                    break;
                }
            }
            // 情形2.1：如果不存在这样的行，则继续循环，处理下一列
            if(k >= m->row){
                j++;
                continue;
            }
            // 情形2.2：如果存在这样的行k，交换第i行和第k行
            row_trans_swap(m, i, k);
            // 后续步骤与情形1相同
            float divisor = m->matrix[i][j];
            for(int t = j; t < m->col; t++){
                m->matrix[i][t] /= divisor;
                if(fabs(m->matrix[i][t]) < __FLT_EPSILON__){
                    m->matrix[i][t] = 0;
                }
            }
            for(int t = i + 1; t < m->row; t++){
                row_trans_sub(m, t, i, m->matrix[t][j]);
            }
            i++;
            j++;
        }
    }
}

void col_trans_swap(matrix *m, int i, int j){
    // 交换两列
    float temp;
    for(int k = 0; k < m->col; k++){
        temp = m->matrix[k][i];
        m->matrix[k][i] = m->matrix[k][j];
        m->matrix[k][j] = temp;
    }
}

void col_trans_sub(matrix *m, int i, int j, float multiple){
    // 两列相减
    for(int k = 0; k < m->col; k++){
        m->matrix[k][i] -= m->matrix[k][j] * multiple;
        if(fabs(m->matrix[k][i]) < __FLT_EPSILON__){
            m->matrix[k][i] = 0;
        }
    }
}

void col_echelon(matrix *m){
    int i = 0;
    int j = 0;
    while(i < m->row && j < m->col){
        // // 情形1：如果matrix[i][j]不为0
        // if(m->matrix[i][j] != 0){
        //     // 首元素置1
        //     float divisor = m->matrix[i][j];
        //     for(int k = i; k < m->row; k++){
        //         m->matrix[k][j] /= divisor;
        //         if(fabs(m->matrix[k][j]) < __FLT_EPSILON__){
        //             m->matrix[k][j] = 0;
        //         }
        //     }
        //     // 同一行右方元素置0
        //     for(int k = j + 1; k < m->col; k++){
        //         col_trans_sub(m, k, j, m->matrix[i][k]);
        //     }
        //     i++;
        //     j++;
        // }
        // // 情形2：如果matrix[i][j]为0
        // else{
        //     // 向右寻找matrix[i][k]不为0的列
        //     int k;
        //     for(k = j + 1; k < m->col; k++){
        //         if(m->matrix[i][k] != 0){
        //             break;
        //         }
        //     }
        //     // 情形2.1：如果不存在这样的列，则继续循环，处理下一行
        //     if(k >= m->col){
        //         i++;
        //         continue;
        //     }
        //     // 情形2.2：如果存在这样的列k，交换第j列和第k列
        //     col_trans_swap(m, j, k);
        //     // 后续步骤与情形1相同
        //     float divisor = m->matrix[i][j];
        //     for(int t = i; t < m->row; t++){
        //         m->matrix[t][j] /= divisor;
        //         if(fabs(m->matrix[t][j]) < __FLT_EPSILON__){
        //             m->matrix[t][j] = 0;
        //         }
        //     }
        //     for(int t = j + 1; t < m->col; t++){
        //         col_trans_sub(m, t, j, m->matrix[i][t]);
        //     }
        //     i++;
        //     j++;
        // }

        // 情形2：如果matrix[i][j]为0
        if(m->matrix[i][j] == 0){
            // 向右寻找matrix[i][k]不为0的列
            int k;
            for(k = j + 1; k < m->col; k++){
                if(m->matrix[i][k] != 0){
                    break;
                }
            }
            // 情形2.1：如果不存在这样的列，则继续循环，处理下一行
            if(k >= m->col){
                i++;
                continue;
            }
            // 情形2.2：如果存在这样的列k，交换第j列和第k列
            col_trans_swap(m, j, k);
        }
        // 情形1和2共有的步骤
        // 首元素置1
        float divisor = m->matrix[i][j];
        for(int k = i; k < m->row; k++){
            m->matrix[k][j] /= divisor;
            if(fabs(m->matrix[k][j]) < __FLT_EPSILON__){
                m->matrix[k][j] = 0;
            }
        }
        // 同一行右方元素置0
        for(int k = j + 1; k < m->col; k++){
            col_trans_sub(m, k, j, m->matrix[i][k]);
        }
        i++;
        j++;
    }
}

int rank(matrix m){
    // 将矩阵转换为行阶梯型
    row_echelon(&m);
    // print_matrix(m);
    // 计算矩阵的秩-->寻找对角线有多少不为0的元素
    int i = 0; 
    int j = 0; 
    while(i < m.row && j < m.col){
        if(m.matrix[i][j] == 0){
            break;
        }
        i++;
        j++;
    }
    return i;
}

int inversion_number(int *array, int N){
    int res = 0;
    for(int i = 0; i < N - 1; i++){
        for(int j = i + 1; j < N; j++){
            if(array[i] > array[j]){
                res++;
            }
        }
    }
    return res;
}

// 计算行列式的辅助函数
int find(int *array, int N, int value){
    // 如果在数组中查找到指定元素，返回true，否则返回false
    for(int i = 0; i < N; i++){
        if(value == array[i]){
            return 1;
        }
    }
    return 0;
}

// 计算行列式的辅助函数
void dfs(float *res, matrix m, int i, int j, int *cols){
    // res用于保存行列式的值，m保存矩阵，i记录当前行，j记录当前列，cols记录哪些列已被选择
    // 终止条件
    if(i == m.row){
        float temp = 1;
        for(int k = 0; k < m.row; k++){
            temp = temp * m.matrix[k][cols[k]];
        }
        *res = *res + pow(-1, inversion_number(cols, m.row)) * temp;
    }
    // 递归
    for(int p = 0; p < m.col; p++){
        // 如果第p列未被选择，则选择第p列，然后递归处理下一行
        if(!find(cols, i, p)){
            cols[i] = p;
            dfs(res, m, i + 1, 0, cols);
            // 回溯
            // do nothing
        }  
    }
}

float det(matrix m){
    // 矩阵必须是方阵
    if(m.row != m.col){
        printf("The matrix is not square matrix(row doesn't equals to column)");
        exit(0);
    }
    // 计算矩阵的行列式
    float res = 0;
    int *cols = (int *)malloc(sizeof(int)*m.row);  //记录哪些列已被选择
    for(int k = 0; k < m.row; k++){
        cols[k] = 0;
    }
    // 递归
    for(int k = 0; k < m.col; k++){
        // 首行选择第k列，然后递归处理下一行
        cols[0] = k; 
        dfs(&res, m, 1, 0, cols);       
        // 回溯
        // do nothing
    }
    return res;
}

float confactor(matrix m, int i, int j){
    // 矩阵必须是方阵
    if(m.row != m.col){
        printf("The matrix is not square matrix(row doesn't equals to column)");
        exit(0);
    }
    matrix remains;
    create(&remains, m.row - 1, m.col - 1);
    for(int p = 0; p < remains.row; p++){
        for(int q = 0; q < remains.col; q++){
            if(p < i && q < j){
                remains.matrix[p][q] = m.matrix[p][q];
            }
            else if(p < i && q >= j){
                remains.matrix[p][q] = m.matrix[p][q + 1];
            }
            else if(p >= i && q < j){
                remains.matrix[p][q] = m.matrix[p + 1][q];
            }
            else if(p >= i && q >= j){
                remains.matrix[p][q] = m.matrix[p + 1][q + 1];
            }
        }
    }
    return det(remains);
}

float algebraic_confactor(matrix m, int i, int j){  
    return confactor(m, i, j)*pow(-1, i+j);
}

matrix inverse(matrix m){
    matrix res;
    create(&res, m.row, m.col);
    for(int i = 0; i < res.row; i++){
        for(int j = 0; j < res.col; j++){
            res.matrix[i][j] = algebraic_confactor(m, j, i) / det(m);
        }
    }
    return res;
}

void print_matrix(matrix m){
    // 输出矩阵
    for(int i = 0; i < m.row; i++){
        for(int j = 0; j < m.col; j++){
            printf("%f ", m.matrix[i][j]);
        }
        printf("\n");
    }
}