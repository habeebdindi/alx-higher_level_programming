#include "lists.h"
/**
 * insert_node - inserts a number in an ordered list.
 * @head: pointer to list head.
 * @number: number to be inserted.
 * Return: pointer to the new node or null if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->next = NULL;
	new->n = number;
	if (!head || !(*head))
	{
		*head = new;
		return (new);
	}
	temp = *head;
	while (temp->next != NULL)
	{
		if ((*head)->n > new->n)
		{
			new->next = *head;
			*head = new;
			break;
		}
		if (temp->next->n > new->n)
		{
			new->next = temp->next;
			temp->next = new;
			break;
		}
		temp = temp->next;
	}
	if (temp->next == NULL)
		temp->next = new;
	return (new);
}
