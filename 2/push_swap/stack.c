/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 18:36:40 by dasantos          #+#    #+#             */
/*   Updated: 2025/12/13 18:46:38 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_node	*new_node(int v)
{
	t_node	*n;

	n = malloc(sizeof(t_node));
	if (!n)
		exit(1);
	n->value = v;
	n->next = NULL;
	return (n);
}

void	add_back(t_node **s, t_node *n)
{
	t_node	*c;

	if (!*s)
	{
		*s = n;
		return ;
	}
	c = *s;
	while (c->next)
		c = c->next;
	c->next = n;
}

int	stack_size(t_node *s)
{
	int	i;

	i = 0;
	while (s)
	{
		i++;
		s = s->next;
	}
	return (i);
}

int	is_sorted(t_node *s)
{
	while (s && s->next)
	{
		if (s->value > s->next->value)
			return (0);
		s = s->next;
	}
	return (1);
}