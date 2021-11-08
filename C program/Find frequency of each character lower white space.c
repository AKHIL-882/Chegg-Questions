// importing the libraries
#include<stdio.h>
#include<string.h>
#include<ctype.h>
void printFrequency(int freq[]){
    for (int i = 0; i < 26; i++) {
        if (freq[i] != 0) {
            printf("Letter %c : %d\n",toupper(i) + 'A', freq[i]);
        }
    }
}
// finding the frequency of the charater
void findFrequncy(char S[]){
    int i = 0;
    int freq[26] = { 0 };
    // Traversing over the string
    while (S[i] != '\0') {
        freq[S[i] - 'a']++;
        i++;
    }
    printFrequency(freq);
}
// initializing the main method
int main(){
    char S[100],j = 0;;
    // getting the string from the user
    printf("Enter String: ");
    gets(S);
    printf("Letter Length: %ld", strlen(S));
    printf("\n");
    // converting to lower case
    char ch,lower[100];
    while (S[j]) {
        ch = S[j];
        lower[j] = tolower(ch);
        j++;
    }
    // removing the white spaces
    int i, countWithSpace=0, countWithoutSpace=0;
    for(i=0; S[i]!='\0'; i++){
        countWithSpace++;
    }
    for(i=0; i<countWithSpace; i++){
        if(S[i]==32)
            countWithoutSpace++;
    }
    countWithoutSpace = countWithSpace-countWithoutSpace;
    printf("\nLetter Length: %d\n", countWithoutSpace);
    findFrequncy(lower);
}

