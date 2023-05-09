#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @head: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
	listint_t *slow_ptr;
	listint_t *fast_ptr;

	slow_ptr = head;
	fast_ptr = head;

	while (head && fast_ptr && fast_ptr->next)
	{
		head = head->next;
		fast_ptr = fast_ptr->next->next;

		if (head == fast_ptr)
		{
			head = slow_ptr;
			slow_ptr =  fast_ptr;
			while (1)
			{
				fast_ptr = slow_ptr;
				while (fast_ptr->next != head && fast_ptr->next != slow_ptr)
				{
					fast_ptr = fast_ptr->next;
				}
				if (fast_ptr->next == head)
					break;

				head = head->next;
			}
			return (1);
		}
	}

	return (0);
}

    

    


