/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fill_b_to_a.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/02 11:17:51 by dasantos          #+#    #+#             */
/*   Updated: 2026/01/02 11:19:05 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include "push_swap.h"

static void set_target_b(t_stack_node *a, t_stack_node *b)
{
    t_stack_node *current_a;
    t_stack_node *target_node;
    long best_match_index;

    while (b)
    {
        best_match_index = LONG_MAX;
        current_a = a;
        while(current_a)
        {
            if (current_a->value > b->value && current_a->value < best_match_index)
            {
                best_match_index = current_a->value;
                target_node = current_a;
            }
            current_a = current_a->next;
        }
       if(best_match_index == LONG_MAX)
            b->target_node = find_min(a);
       else
        b->target_node = target_node;
       b = b->next;
    }
}
void fill_nodes_b(t_stack_node *a, t_stack_node *b)
{
    current_index(a);
    current_index(b);
    set_target_b(a, b);

}