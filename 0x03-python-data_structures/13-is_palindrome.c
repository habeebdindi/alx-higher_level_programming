#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of the list.
 * Return: 1 if it is a palindrome and 0 if it is not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *sec_half, *first_half;

	if (!head || !*head ||!(*head)->next)
		return (1);
	slow = fast = *head;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast != NULL)
		sec_half = slow->next;
	else
		sec_half = slow;
	reverse_list(&sec_half);
	first_half = *head;
	while (sec_half != NULL)
	{
		if (first_half->n != sec_half->n)
			return (0);
		first_half = first_half->next;
		sec_half = sec_half->next;
	}
	return (1);
}

/**
 * reverse_list - reverses a singly linked list.
 * @head: a pointer to the head of the list to be reversed.
 * Return: void.
 */
void reverse_list(listint_t **head)
{
	listint_t *current, *prev, *next;

	if (!(*head))
		return;
	current = *head;
	prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
