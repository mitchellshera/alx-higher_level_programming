#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
  *
   * @h: Double pointer to a singly linked list
    *
     * @num: Value of the new node.
      *
       * Return: The address of the new node, or NULL if it failed.
        */

        listint_t *insert_node(listint_t **h, int num)
        {
            int f = 0;
                listint_t *new_node = NULL, *cur = NULL, *next = NULL;

                    if (h == NULL)
                            return (NULL);
                                new_node = malloc(sizeof(listint_t));
                                    if (!new_node)
                                            return (NULL);
                                                new_node->n = num, new_node->next = NULL;
                                                    if (*h == NULL)
                                                        {
                                                                *h = new_node;
                                                                        return (*h);
                                                                            }
                                                                                cur = *h;
                                                                                    if (num <= cur->n)
                                                                                        {
                                                                                                new_node->next = cur, *h = new_node;
                                                                                                        return (*h);
                                                                                                            }
                                                                                                                if (num > cur->n && !cur->next)
                                                                                                                    {
                                                                                                                            cur->next = new_node;
                                                                                                                                    return (new_node);
                                                                                                                                        }
                                                                                                                                            next = cur->next;
                                                                                                                                                while (cur)
                                                                                                                                                    {
                                                                                                                                                            if (!next)
                                                                                                                                                                        cur->next = new_node, f = 1;
                                                                                                                                                                                else if (next->n == num)
                                                                                                                                                                                            cur->next = new_node, new_node->next = next, f = 1;
                                                                                                                                                                                                    else if (next->n > num && cur->n < num)
                                                                                                                                                                                                                cur->next = new_node, new_node->next = next, f = 1;
                                                                                                                                                                                                                        if (f)
                                                                                                                                                                                                                                    break;
                                                                                                                                                                                                                                            next = next->next, cur = cur->next;
                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                    return (new_node);
                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                    