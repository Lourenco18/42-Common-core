/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_small.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 18:36:38 by dasantos          #+#    #+#             */
/*   Updated: 2025/12/13 18:46:43 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	min_pos(t_node *a)
{
	int	m;
	int	i;
	int	p;

	m = a->value;
	i = 0;
	p = 0;
	while (a)
	{
		if (a->value < m)
		{
			m = a->value;
			p = i;
		}
		i++;
		a = a->next;
	}
	return (p);
}

void	sort_small(t_node **a, t_node **b)
{
	int p;

	while (stack_size(*a) > 3)
	{
		p = min_pos(*a);
		if (p == 0)
			pb(a, b);
		else
			ra(a);
	}
	if (!is_sorted(*a))
		sa(a);
	while (*b)
		pa(a, b);
}