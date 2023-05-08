#include "lists.h"

/**
 * check_cycle - checks if a list is a cycle.
 * @list: pointer to the head of the list.
 * Return: 0 if there is no cycle, and 1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (!list)
		return (0);
	temp = malloc(sizeof(listint_t));
	if (!temp)
		return (0);
	temp = list;
	temp = temp->next;
	while (temp != NULL)
	{
		if (temp == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
