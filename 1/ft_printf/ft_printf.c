/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 12:20:26 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/22 12:25:52 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
// vou usar a libft:
//  ft_putchar_fd.c
//  ft_putstr_fd.c
//  ft_putnbr_fd.c
//  novas funcoes:
//  ft_puthex_fd.c
//  ft_putptr_fd.c
// ft_putunbr_fd.c

static int ft_formats(va_list args, const char format)
{
    int count;

    count = 0;
    if (format == 'c')
        count += ft_putchar(va_arg(args, int));
    else if (format == 's')
        count += ft_putstr(va_arg(args, char *));
    else if (format == 'p')
        count += ft_putptr(va_arg(args, void *));
    else if (format == 'd' || format == 'i')
        count += ft_putnbr(va_arg(args, int));
    else if (format == 'u')
        count += ft_putunbr(va_arg(args, unsigned int));
    else if (format == 'x' || format == 'X')
        count += ft_puthex(va_arg(args, unsigned int), format);
    else if (format == '%')
        count += ft_putchar('%');
    return (count);
}

int ft_printf(const char *fmt, ...)
{
    va_list args;
    int i;
    int count;

    i = 0;
    count = 0;
    va_start(args, fmt);
    while (fmt[i])
    {
        if (fmt[i] == '%' && fmt[i + 1])
        {
            i++;
            count += ft_formats(args, fmt[i]);
        }
        else
            count += ft_putchar(fmt[i]);
        i++;
    }
    va_end(args);
    return (count);
}
