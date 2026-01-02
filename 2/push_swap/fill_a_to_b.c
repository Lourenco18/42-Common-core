/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fill_a_to_b.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/02 10:52:17 by dasantos          #+#    #+#             */
/*   Updated: 2026/01/02 11:05:34 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void current_index(t_stack_node *stack)
{
    int i;
    int mediam;

    i = 0;
    if(!stack)
        return ;
    mediam = stack_len(stack) / 2;
    while (stack)
    {
        stack->index = i;
        if( i <= mediam)
            stack->above_median = true;
        else
            stack->above_median = false;
        
        stack = stack->next;
        i++;
    }
}

static void set_target_a(t_stack_node *a, t_stack_node *b)
{
    t_stack_node *current_b;
    t_stack_node *target_node;
 long best_match_index;

    while (a)
    {
        best_match_index = LONG_MIN;
        current_b = b;
        while(current_b)
        {
            if (current_b->value < a->value && current_b->value > best_match_index)
            {
                best_match_index = current_b->value;
                target_node = current_b;
            }
            current_b = current_b->next;
        }
       if(best_match_index == LONG_MIN)
            a->target_node = find_max(b);
       else
        a->target_node = target_node;
       a = a->next;

    }
 
}

static void cost_a(t_stack_node *a, t_stack_node *b)
{
   int len_a;
    int len_b;

    len_a = stack_len(a);
    len_b = stack_len(b);
    while (a)
    {
        a->push_cost = a->index;
        if(!(a->above_median))
            a->push_cost = len_a - (a->index);
        if(a->target_node->above_median)
        {
            a->push_cost += a->target_node->index;
        }
        else
        {
            a->push_cost += len_b - (a->target_node->index);
        }
        a = a->next;
    }
}

void set_cheapest(t_stack_node *stack)
{
    t_stack_node *cheapest_node;
    long cheapest_value;

    if(!stack)
        return ;
   cheapest_value = LONG_MAX;
    while (stack)
    {
        if(stack->push_cost < cheapest_value)
        {
            cheapest_value = stack->push_cost;
            cheapest_node = stack;
        }
        stack = stack->next;
    }
    cheapest_node->cheapest = true;
}

void fill_nodes_a(t_stack_node *a, t_stack_node *b)
{
    current_index(a);
    current_index(b);
    set_target_a(a, b);
    cost_a(a, b);
    set_cheapest(a);
}