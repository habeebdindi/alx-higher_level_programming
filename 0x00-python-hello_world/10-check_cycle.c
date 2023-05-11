#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a list is a cycle.
 * @list: pointer to the head of the list.
 * Return: 0 if there is no cycle, and 1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *one_step, *two_steps;

	if (!list)
		return (0);
	one_step = two_steps = list;
	while (one_step && two_steps && two_steps->next)
	{
		one_step = one_step->next;
		two_steps = two_steps->next->next;
		if (one_step == two_steps)
			return (1);
	}
	return (0);
}
