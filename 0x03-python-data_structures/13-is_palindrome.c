#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palidrome
 * @head: pointer to the list
 *
 * Return: 0 if not a palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{

	int size = 0;
	int array[3000];
	int i;

	if (!head || !(*head) || (*head)->next == NULL)
		return (1);
	while (*head)
	{
		array[size] = (*head)->n;
		*head = (*head)->next;
		size++;
	}
	for (i = 0; i < size; i++)
	{
		if (array[i] != array[(size - 1) - i])
		{
			return (0);
		}
	}
	return (1);
}
