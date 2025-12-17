/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 18:36:18 by dasantos          #+#    #+#             */
/*   Updated: 2025/12/13 18:46:54 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	error_exit(void)
{
	write(2, "Error\n", 6);
	exit(1);
}

int	main(int ac, char **av)
{
	t_node *a;
	t_node *b;

	a = NULL;
	b = NULL;
	if (ac < 2)
		return (0);
	if (!parse_args(ac, av, &a))
		error_exit();
	if (is_sorted(a))
		return (0);
	if (stack_size(a) <= 5)
		sort_small(&a, &b);
	else
		sort_big(&a, &b);
	return (0);
}