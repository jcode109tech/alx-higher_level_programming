#include<stdlib.h>
#include "lists.h"

    // Function to check if a linked list is a palindrome
int is_palindrome(listint_t **head) 
{
    // Check if the linked list is empty or has only one node
    if (*head == NULL || (*head)->next == NULL) 
        return 1; // Empty list or single node is considered a palindrome

    // Initialize two pointers for traversing the list
    listint_t *slow = *head;
    listint_t *fast = *head;

    // Move slow pointer one step and fast pointer two steps
    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse the second half of the list
    listint_t *prev = NULL;
    listint_t *current = slow;
    listint_t *next;

    while (current != NULL) 
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    // Compare the reversed second half with the first half
    listint_t *firstHalf = *head;
    listint_t *secondHalf = prev;

    while (secondHalf != NULL)
    {
        if (firstHalf->n != secondHalf->n)
            return 0; // Not a palindrome
        
        firstHalf = firstHalf->next;
        secondHalf = secondHalf->next;
    }

    return 1; // Palindrome
}
