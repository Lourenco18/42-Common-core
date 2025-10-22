/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_puthex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 12:10:55 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/22 12:18:30 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
// escrever em hexadecimal
int ft_puthex(unsigned int n, const char format)
{
    int count;
    char *base;

    count = 0;
    if (format == 'x')
        base = "0123456789abcdef";
    else
        base = "0123456789ABCDEF";
    if (n >= 16)
        count += ft_puthex(n / 16, format);
    count += ft_putchar(base[n % 16]);
    return (count);
}
