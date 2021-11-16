// importing the libraries
#include <stdio.h>
#include <string.h>
// main function
int main(){
    // message
    char message[] = ")& ! 7//$#(5#+ #/5,$ #(5#+ 7//$, (/7 -5#( 7//$ 7/5,$ ! 7//$#(5#+ #(5#+?";
    // local variables
    char test[100];
    int i, j;
    // for loop for iterating over alphabets
    for (i = 0; i < 26; i++) {
        // decoding the messaage
        int offset = 'a' - message [0] + i;
        for (j = 0; j < strlen (message); j++)
            if ((message[j] == ' ') || (message[j] == '?')) // Punctuation & space 
                test [j] = message [j];
            else if ((message [j] == ',') && (message [j+1] == ' ')) // Comma at end of word
                test [j] = message [j];
            else            
                test[j] = message[j] + offset;
        test [j] = '\0';
        // displaying the result
        printf ("%s\n", test);
    }
    return 0;
}