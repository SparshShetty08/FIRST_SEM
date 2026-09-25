#include<stdio.h>
int main(){
    char choice;
    int i;
    int j;
    
    printf("----Welcome to my Calculator----\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("Enter your choice:");
    scanf(" %c"),&choice;
    printf("Enter the first number:");
    scanf("%d",&i);
    printf("Enter the second number:");
    scanf("%d",&j);
    if(choice=='+'){
        printf("The sum of %d and %d is %d\n",i,j,i+j);
    }
    else if(choice=='-'){
        printf("The difference between %d and %d is %d\n",i,j,i-j);
    }
    else if(choice=='*'){
        printf("The product of %d and %d is %d\n",i,j,i*j);
    }
    else if(choice=='/'){
        if(j!=0){
            printf("The quotient of %d and %d is %f\n",i,j,(float)i/j);
        }
        else{
            printf("Error: Division by zero is not allowed.\n");
        }
    }
    else{
        printf("Invalid choice. Please select a valid operation.\n");
    }
    





}