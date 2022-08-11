#include"DataStructure/AList_update.h"

int main(){
    AList alist = create(3);
    DataType stud1 = {"20181745", "ycl", "male", 21, "5ban"};
    DataType stud2 = {"20181750", "ydx", "male", 23, "5ban"};
    DataType stud3 = {"20181736", "wdl", "male", 22, "5ban"};
    append(&alist, stud1);
    append(&alist, stud2);
    append(&alist, stud3);
    traverse(alist);
    return 0;
}