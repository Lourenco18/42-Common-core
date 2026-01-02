/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/02 11:12:04 by dasantos          #+#    #+#             */
/*   Updated: 2026/01/02 11:15:25 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

# include "push_swap.h"
void ra(t_stack_node **a, bool print){
    rotate(a);
    if(!print)
        ft_printf("ra\n");
}

void rb(t_stack_node **b, bool print){
    rotate(b);
    if(!print)
        ft_printf("rb\n");
}

void rr(t_stack_node **a, t_stack_node **b, bool print){
    rotate(a);
    rotate(b);
    if(!print)
        ft_printf("rr\n");
}

void rotate_both(t_stack_node **a, 
                t_stack_node **b, 
                t_stack_node *cheapest_node){
    while(*b != cheapest_node->target_node && 
          (*a) != cheapest_node)
    {
        rr(a, b, false);
   current_index(*a);
    current_index(*b);
    }
}