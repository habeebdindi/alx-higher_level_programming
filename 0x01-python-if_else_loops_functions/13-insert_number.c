#inlcude "lists.h"
/**
 * insert_node - inserts a number in an ordered list.
 * @head: pointer to list head.
 * @number: number to be inserted.
 * Return: pointer to the new node or null if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, **temp;

	if (!head)
		return (NULL);
	temp = head;
	while (*temp != NULL)
	{
		if (number < (*temp)->num)
		{
			new = malloc(sizeof(listint *));
			if (!new)
				return (NULL);
			new->next = (*temp)->next;
			new->n = number;
			(*temp)->next = new;
		}
		*temp = (*temp)->next;
	}
	free(new);
	return (new);
}
