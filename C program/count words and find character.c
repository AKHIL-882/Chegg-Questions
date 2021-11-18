// importing the libaries
#include <stdio.h>
// function to count the words in the line
int countWords(char string[]){
  int i=0;
  int count=0;
  while(string[i]!='\0') {
    if(string[i]==' ') {
      count++; 
    }
    i++;
  }
  count++; 
  return count;
}
// initializing the main method
int main(void) {
  // local variables
  char string[100];
  printf("Enter string with spaces:\n");
  fgets(string, sizeof(string), stdin); 
  printf("Give me the search character: ");
  char c;
  scanf("%c",&c); 
  int i=0;
  int wordsCount=-1; 
  while(string[i]!='\0'){
    if(string[i]==c){
      wordsCount=countWords(string); 
      break;
    }
    i++;
  }
  if(wordsCount!=-1) 
  printf("\nThe line of text contains %d words",wordsCount);
  else{
    printf("\nThe line of text provided doesn't contain the character \'%c\'",c);
  }
}