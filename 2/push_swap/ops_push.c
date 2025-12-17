/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ops_push.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 18:36:21 by dasantos          #+#    #+#             */
/*   Updated: 2025/12/13 18:46:51 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	pb(t_node **a, t_node **b)
{
	t_node	*n;

	if (!*a)
		return ;
	n = *a;
	*a = (*a)->next;
	n->next = *b;
	*b = n;
	write(1, "pb\n", 3);
}

void	pa(t_node **a, t_node **b)
{
	t_node *n;

	if (!*b)
		return ;
	n = *b;
	*b = (*b)->next;
	n->next = *a;
	*a = n;
	write(1, "pa\n", 3);
}