/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 11:11:46 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/23 11:11:47 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdio.h>

int main(void)
{
    ft_printf("Meu printf: %d %x %s %p %%\n", 42, 42, "teste", &main);
    printf("Original  : %d %x %s %p %%\n", 42, 42, "teste", &main);
    return (0);
}
