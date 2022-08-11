#include"../DataStructure/LStack_update.h"

int main(){
    LStack s = create(3);
    DataType stud1 = {"20181745", "ycl", "male", 21, "5ban"};
    DataType stud2 = {"20181750", "ydx", "male", 23, "5ban"};
    DataType stud3 = {"20181736", "wdl", "male", 22, "5ban"};
    push(&s, stud1);
    push(&s, stud2);
    push(&s, stud3);
    while(s.top != NULL){
        DataType temp = pop(&s);
        printf("%s\t", temp.studentID);
        printf("%s\t", temp.studentName);
        printf("%s\t", temp.sex);
        printf("%d\t", temp.age);
        printf("%s\n", temp.class);
    }
    return 0;
}