#include <stddef.h>
#include <stdlib.h>
#include "lists.h" 

/**
 * insert_node - inserts a number in a sorted singly linked list
 * @head: pointer to pointer of the first node
 * @number: integer to insert
 * Return: address of new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;

	if (!*head)
	{
		new->next = *head;
		*head = new;
		return (new);
	}


	for (temp = *head; temp != NULL; temp = temp->next)
	{
		if (temp->n <= number && (temp->next)->n >= number)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		else if (temp->n > number)
		{
			new->next = temp;
			*head = new;
			return (new);
		}
	}
	return (NULL);
}
