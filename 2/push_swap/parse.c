/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 18:36:26 by dasantos          #+#    #+#             */
/*   Updated: 2025/12/13 18:46:48 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	atoi_safe(char *s, int *n)
{
	long	r;
	int		sign;

	r = 0;
	sign = 1;
	if (*s == '-' || *s == '+')
	{
		if (*s == '-')
			sign = -1;
		s++;
	}
	if (!*s)
		return (0);
	while (*s)
	{
		if (*s < '0' || *s > '9')
			return (0);
		r = r * 10 + (*s - '0');
		if (r * sign > INT_MAX || r * sign < INT_MIN)
			return (0);
		s++;
	}
	*n = r * sign;
	return (1);
}

int	parse_args(int ac, char **av, t_node **a)
{
	int i;
	int v;

	i = 1;
	while (i < ac)
	{
		if (!atoi_safe(av[i], &v))
			return (0);
		add_back(a, new_node(v));
		i++;
	}
	return (1);
}