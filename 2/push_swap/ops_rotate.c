/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_rotate.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 18:36:22 by dasantos          #+#    #+#             */
/*   Updated: 2025/12/13 18:46:50 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ra(t_node **a)
{
	t_node	*f;
	t_node	*l;

	if (!*a || !(*a)->next)
		return ;
	f = *a;
	*a = f->next;
	l = *a;
	while (l->next)
		l = l->next;
	l->next = f;
	f->next = NULL;
	write(1, "ra\n", 3);
}

void	rra(t_node **a)
{
	t_node *p;
	t_node *l;

	if (!*a || !(*a)->next)
		return ;
	p = NULL;
	l = *a;
	while (l->next)
	{
		p = l;
		l = l->next;
	}
	p->next = NULL;
	l->next = *a;
	*a = l;
	write(1, "rra\n", 4);
}