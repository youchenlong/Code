#include"../DataStructure/Graphm.h"

int main(){
    Graphm g = create_Graphm(5);
    setEdge(&g, 0, 1, 1);
    setEdge(&g, 0, 4, 1);
    setEdge(&g, 1, 3, 1);
    setEdge(&g, 2, 4, 1);
    setEdge(&g, 3, 2, 1);
    setEdge(&g, 4, 1, 1);
    for(int i = 0; i < n(g); i++){
        for(int j = 0; j < n(g); j++){
            printf("%d\t", getWeight(g, i, j));
        }
        printf("\n");
    }
    printf("%d\n", firstNeighbor(g, 0));
    printf("%d\n", nextNeighbor(g, 0, 1));
    return 0;
}