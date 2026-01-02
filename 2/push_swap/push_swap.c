/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/29 11:53:00 by dasantos          #+#    #+#             */
/*   Updated: 2026/01/02 10:41:23 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"



int	main(int argc, char **argv)
{
	t_stack_node	*a;
	t_stack_node	*b;

	a = NULL;
	b = NULL;
	if (argc == 1 || (argc == 2 && !argv[1][0])){
		return (1);
	}else if(argc == 2){
		argv = ft_split(argv[1], ' ');
	}
	fill_stack_a(&a, argv +1);
	if(!stack_sorted(a)){
		if(stack_len(a)== 2){
			sa(&a, false);
		}else if(stack_len(a) == 3){
			sort_three(&a);
		}else{
			sort_stacks(&a, &b);
		}
	}
		free_stack(&a);

	return (0);
}
