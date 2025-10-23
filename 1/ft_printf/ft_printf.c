/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 11:10:07 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/23 11:13:30 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int conversao(char format, va_list args)
{
    if (format == '%')
        return (write(1, "%", 1)); /* imprime o caractere '%'  caso seja "%%"*/
    else if (format == 'c')        /* caractere */
        return (ft_putchar(va_arg(args, int)));
    else if (format == 's') /* string */
        return (ft_putstr(va_arg(args, char *)));
    else if (format == 'p') /* ponteiro */
        return (ft_putptr(va_arg(args, void *)));
    else if (format == 'd' || format == 'i')
        return (ft_putnbr(va_arg(args, int)));
    else if (format == 'u') /* inteiro sem sinal */
        return (ft_putunbr(va_arg(args, unsigned int)));
    else if (format == 'x') /* hexadecimal minúsculo */
        return (ft_puthex(va_arg(args, unsigned int), 0));
    else if (format == 'X') /* hexadecimal maiúsculo */
        return (ft_puthex(va_arg(args, unsigned int), 1));
    return (0);
}

int ft_printf(const char *format, ...)
{
    int i;
    int len;
    va_list args; /* lista de argumentos variaveis */

    if (!format) /* se o formato for NULL, retorna 0 */
        return (0);
    i = 0;
    len = 0;
    va_start(args, format); /* inicializa a lista de argumentos */
    while (format[i])
    {
        if (format[i] == '%') /* encontrou um especificador de formato */
        {
            i++;
            len += conversao(format[i], args); /* processa a conversão */
        }
        else
            len += write(1, &format[i], 1); /* escreve caractere normal */
        i++;
    }
    va_end(args); /* finaliza a lista de argumentos */
    return (len);
}
