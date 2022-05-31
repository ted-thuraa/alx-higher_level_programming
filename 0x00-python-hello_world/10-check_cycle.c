#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks for cycle in a linked list
 * @list: pointer to the list
 * return: 0 if no cycle or 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
	{
		return (0);
	}

	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
