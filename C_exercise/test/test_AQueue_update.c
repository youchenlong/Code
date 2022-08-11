#include"../DataStructure/AQueue_update.h"

int main(){
    AQueue q = create(3);
    DataType stud1 = {"20181745", "ycl", "male", 21, "5ban"};
    DataType stud2 = {"20181750", "ydx", "male", 23, "5ban"};
    DataType stud3 = {"20181736", "wdl", "male", 22, "5ban"};
    enqueue(&q, stud1);
    enqueue(&q, stud2);
    enqueue(&q, stud3);
    while(length(q) != 0){
        DataType temp = dequeue(&q);
        printf("%s\t", temp.studentID);
        printf("%s\t", temp.studentName);
        printf("%s\t", temp.sex);
        printf("%d\t", temp.age);
        printf("%s\n", temp.class);
    }
    return 0;
}