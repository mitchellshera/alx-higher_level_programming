#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
  * @head: double pointer to the head of the list
   *
    * Return: 0 if not a palindrome, 1 if a palindrome
     */
     int is_palindrome(listint_t **head)
     {
         listint_t *slow = *head;
             listint_t *fast = *head;
                 listint_t *prev = NULL;
                     listint_t *next = NULL;

                         if (*head == NULL || (*head)->next == NULL)
                                 return (1);

                                     while (fast != NULL && fast->next != NULL)
                                         {
                                                 fast = fast->next->next;
                                                         prev = slow;
                                                                 slow = slow->next;
                                                                     }

                                                                         if (fast != NULL)
                                                                                 slow = slow->next;

                                                                                     while (slow != NULL)
                                                                                         {
                                                                                                 next = slow->next;
                                                                                                         slow->next = prev;
                                                                                                                 prev = slow;
                                                                                                                         slow = next;
                                                                                                                             }

                                                                                                                                 fast = *head;
                                                                                                                                     slow = prev;
                                                                                                                                         while (slow != NULL)
                                                                                                                                             {
                                                                                                                                                     if (fast->n != slow->n)
                                                                                                                                                                 return (0);
                                                                                                                                                                         fast = fast->next;
                                                                                                                                                                                 slow = slow->next;
                                                                                                                                                                                     }

                                                                                                                                                                                         return (1);
                                                                                                                                                                                         }
                                                                                                                                                                                         