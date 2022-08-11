#include<stdio.h>

int main(){
    int num = 16;
    // float credit[8] = {2, 2, 2, 2, 3, 3, 3, 2};
    // float score[8] = {91, 91, 69, 93, 86, 93, 84, 91};
    // float credit[8] = {2, 3, 2, 2, 3, 2, 3, 2};
    // float score[8] = {85, 97, 92, 86, 92, 94, 91, 80};
    float credit[16] = {2, 2, 2, 2, 3, 3, 3, 2, 2, 3, 2, 2, 3, 2, 3, 2};
    float score[16] = {91, 91, 69, 93, 86, 93, 84, 91, 85, 97, 92, 86, 92, 94, 91, 80};
    float grade_point = 0;
    float total_credit = 0;
    float weighted_score = 0;
    for(int i = 0; i < num; i++){
        total_credit += credit[i];
    }
    for(int i = 0; i < num; i++){
        if(score[i] >= 90 && score[i] <= 100){
            weighted_score = weighted_score + 4 * credit[i];
        }
        else if(score[i] >= 80 && score[i] < 90){
            weighted_score = weighted_score + ((score[i] - 80) / 10 + 3) * credit[i];
        }
        else if(score[i] >= 70 && score[i] < 80){
            weighted_score = weighted_score + ((score[i] - 70) / 10 + 2) * credit[i];
        }
        else if(score[i] >= 60 && score[i] < 70){
            weighted_score = weighted_score + ((score[i] - 60) / 10 + 1) * credit[i];
        }  
    }
    grade_point = weighted_score / total_credit;
    printf("%f", grade_point);
    return 0;
}