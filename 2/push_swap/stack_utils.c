/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_utils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/02 10:42:49 by dasantos          #+#    #+#             */
/*   Updated: 2026/01/02 10:44:54 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

bool stack_sorted(t_stack_node *stack)
{


    if (!stack)
        return (1);
 
    while (stack->next)
    {
        if (stack->value > stack->next->value)
            return (false);
        stack = stack->next;
    }
    return (true);
}

t_stack_node *find_min(t_stack_node *stack)
{
    long min;
    t_stack_node *min_node;

    if (!stack)
        return (NULL);
    min = LONG_MAX;
    while (stack)
    {
        if (stack->value < min)
        {
            min = stack->value;
            min_node = stack;
        }
        stack = stack->next;
    }
    return (min_node);
}