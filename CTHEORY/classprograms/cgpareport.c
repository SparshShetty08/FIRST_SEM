#include <stdio.h>
void addition(float marks, float total, float average, float cgpa){
    total += marks;
    average = total / 5;
    cgpa = average / 9.5;
}
int main(){
    int roll;
    float marks,total,average,cgpa;
    total = 0;
    average = 0;
    cgpa = 0;
    for (int i = 1;i<=3;i++){
     printf("Enter details of Student %d\n",i);
     printf("Enter roll number: ");
     scanf("%d",&roll);
     for (int j=1;j<=5;j++){
          printf("Enter marks: ");
          scanf("%f",&marks);
          addition(marks,total,average,cgpa);
     }
    printf("Total{%d}: %.2f\n",i, total);
    printf("Average{%d}: %.2f\n",i, average);
    printf("CGPA{%d}: %.2f\n",i, cgpa);
    }
    return 0;
}