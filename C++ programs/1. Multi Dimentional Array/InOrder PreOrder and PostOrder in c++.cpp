
#include <iostream>
using namespace std;
struct Node {
    int data;
    struct Node *left, *right;
};

Node* newNode(int data){
    Node* temp = new Node;
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;
}

void displayPostOrder(struct Node* node){
    if (node == NULL)
        return;
    displayPostOrder(node->left);
    displayPostOrder(node->right);
    cout << node->data << " ";
}
void displayInorder(struct Node* node){
    if (node == NULL)
        return;
    displayInorder(node->left);
    cout << node->data << " ";
    displayInorder(node->right);
}
void printPreOrder(struct Node* node){
    if (node == NULL)
        return;
    cout << node->data << " ";
    printPreOrder(node->left);
    printPreOrder(node->right);
}

int main(){
    struct Node* root = newNode(33);
    root->left = newNode(29);
    root->right = newNode(47);
    root->right->left = newNode(34);
    root->left->left = newNode(13);
    root->left->right = newNode(30);
    root->left->left->left = newNode(8);
    
 
    cout << "\nPreorder traversal of binary tree is \n";
    printPreOrder(root);
 
    cout << "\nInorder traversal of binary tree is \n";
    displayInorder(root);
 
    cout << "\nPostorder traversal of binary tree is \n";
    displayPostOrder(root);
 
    return 0;
}