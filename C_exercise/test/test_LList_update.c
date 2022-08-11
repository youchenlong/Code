#include"../DataStructure/LList_update.h"

int main(){
    LList llist = create();
    DataType stud1 = {"20181745", "ycl", "male", 21, "5ban"};
    DataType stud2 = {"20181750", "ydx", "male", 23, "5ban"};
    DataType stud3 = {"20181736", "wdl", "male", 22, "5ban"};
    append(&llist, stud1);
    append(&llist, stud2);
    append(&llist, stud3);
    // traverse(llist);
    printf("currPos=%d\n", currPos(llist));
    return 0;
}