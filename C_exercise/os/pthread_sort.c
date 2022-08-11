#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<unistd.h>
#include<pthread.h>

struct array{
    int *a;
    int N;
};

void print(int a[], int N){
    for(int i = 0; i < N; i++){
        for(int j = 0; j < a[i]; j++){
            printf("*");
        }
        printf("\n");
    }
    printf("-------------------------\n");
}

void *bubble_sort(void *arg){
    struct array *bubble_array = (struct array *)arg;
    for(int i = 0; i < bubble_array->N-1; i++){
        for(int j = 0; j < bubble_array->N-1-i; j++){
            if(bubble_array->a[j] > bubble_array->a[j+1]){
                int temp = bubble_array->a[j+1];
                bubble_array->a[j+1] = bubble_array->a[j];
                bubble_array->a[j] = temp;
            }
            usleep(500000);
            printf("bubble_sort\n");
            print(bubble_array->a, 10);
        }
    }
}

void *insert_sort(void *arg){
    struct array *insert_array = (struct array *)arg;
    for(int i = 0; i < insert_array->N; i++){
        for(int j = i; j > 0; j--){
            if(insert_array->a[j-1] > insert_array->a[j]){
                int temp = insert_array->a[j];
                insert_array->a[j] = insert_array->a[j-1];
                insert_array->a[j-1] = temp;
            }
            usleep(500000);
            printf("insert_sort\n");
            print(insert_array->a, 10);
        }
    }
}

int main(){
    srand((unsigned)time(NULL));
    int a[10];
    int b[10];
    for(int i = 0; i < 10; i++){
        a[i] = rand() % 10;
        b[i] = a[i];
    }  
    struct array bubble_array, insert_array;
    bubble_array.a = a;
    bubble_array.N = 10;
    insert_array.a = b;
    insert_array.N = 10;
    pthread_t tid_bubble_sort, tid_insert_sort;
    pthread_create(&tid_bubble_sort, 0, bubble_sort, &bubble_array);
    pthread_create(&tid_insert_sort, 0, insert_sort, &insert_array);
    pthread_join(tid_bubble_sort, NULL);
    pthread_join(tid_insert_sort, NULL);
    return 0;
}