/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/13 18:36:34 by dasantos          #+#    #+#             */
/*   Updated: 2025/12/13 18:46:46 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H
# include <limits.h>
# include <stdlib.h>
# include <unistd.h>

typedef struct s_node
{
	int				value;
	struct s_node	*next;
}					t_node;

/* parse */
int					parse_args(int ac, char **av, t_node **a);

/* stack */
t_node				*new_node(int v);
void				add_back(t_node **s, t_node *n);
int					stack_size(t_node *s);
int					is_sorted(t_node *s);

/* operations */
void				sa(t_node **a);
void				pa(t_node **a, t_node **b);
void				pb(t_node **a, t_node **b);
void				ra(t_node **a);
void				rra(t_node **a);

/* sort */
void				sort_small(t_node **a, t_node **b);
void				sort_big(t_node **a, t_node **b);

/* utils */
void				error_exit(void);

#endif