// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int a,b,c,d;
    a = 0;
    b = 0;
    c = 5;
    d = 6;
    printf("PATTERN\n");
    while(a<5){
        b = 0;
        while(b<=d){
            if(b>c){
                printf("*");
                
            }else{
                printf(" ");
            }
            // printf(" %d %d",a,b);
            b++;
        }
        printf("\n");
        a++;
        d++;
        c--;
    }
    
    // Write C code here
    

    return 0;
}
