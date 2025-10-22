/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 12:34:17 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/22 12:34:18 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdio.h>

int main(void)
{
    ft_printf("Meu printf: %d %x %s\n", 42, 42, "teste");
    printf("Original  : %d %x %s\n", 42, 42, "teste");
    return 0;
}
