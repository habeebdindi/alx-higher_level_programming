#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a list is a cycle.
 * @list: pointer to the head of the list.
 * Return: 0 if there is no cycle, and 1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *check;

	if (!list)
		return (0);
	temp = list;
	temp = temp->next;
	while (temp != NULL)
	{
		check = list;
		while (check->next != temp)
		{
			if (temp == check)
				return (1);
			check = check->next;
		}
		temp = temp->next;
	}
	return (0);
}
