// importing the libraries
#include<stdio.h>
#include <stdlib.h>
// function to count the letters
int * lettersCount(char word[]){
    int *arr = (int*)(malloc(26*sizeof(int)));
    printf("%s\n",word);
    for(int i=0;i<26;i++){
        arr[i] = 0;
    }

    int i=0;
    while(word[i]!='\0'){
        arr[word[i++]-'A']++;
    }

    return arr;
}
// function to print the character
void characterPrint(int arr[]){
    for(int i=0;i<26;i++){
        if(arr[i]>0){
            printf("%c: %d, ",('A'+i),arr[i]);
        }
    }
    printf("\n");
}

// main method
int main(){
    char names[6][20];
    
    // getting Father's name
    printf("Enter father's first name : ");
    scanf("%s",names[0]);
    printf("Enter father's last name : ");
    scanf("%s",names[1]);

    //  getting  Mother's name
    printf("Enter mother's's first name : ");
    scanf("%s",names[2]);
    printf("Enter mother's last name : ");
    scanf("%s",names[3]);


    // getting  Sister's name
    printf("Enter sister's first name : ");
    scanf("%s",names[4]);
    printf("Enter sister's last name : ");
    scanf("%s",names[5]);


    printf("\n\nFather's first name letter count  : ");
    characterPrint(lettersCount(names[0]));
    printf("Father's last name letter count  : ");
    characterPrint(lettersCount(names[1]));


    printf("\n\nMother's name letter count  : ");
    characterPrint(lettersCount(names[2]));
    printf("Mother's last name letter count  : ");
    characterPrint(lettersCount(names[3]));


    printf("\n\nSister's first name letter count  : ");
    characterPrint(lettersCount(names[4]));
    printf("Sister's last name letter count  : ");
    characterPrint(lettersCount(names[5]));
    return 0;
}
