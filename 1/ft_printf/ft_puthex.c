/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_puthex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 10:28:55 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/23 11:11:14 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

/*
Conta quantos dígitos hexadecimais são necessários
n = 255 → "ff" → 2 dígitos.
*/
static size_t count_hex_digits(unsigned int n)
{
    size_t count;

    count = 0;
    if (n == 0)
        return (1);
    while (n > 0) /* calcular quantos dígitos são necessários */
    {
        n /= 16;
        count++;
    }
    return (count);
}

/*
Imprime o número em hexadecimal, um dígito de cada vez.
É recursiva — ou seja, chama-se a si mesma até que o número seja < 16.
'uppercase' indica se queremos letras maiúsculas (1) ou minúsculas (0).
*/
static void print_hex_recursive(unsigned int n, int uppercase)
{
    const char *base;

    /* Escolher qual conjunto de caracteres usar*/
    if (uppercase) /* caso seja maiúsculas*/
        base = "0123456789ABCDEF";
    else
        base = "0123456789abcdef";

    /* Chama recursivamente até chegar ao primeiro dígito */
    if (n >= 16)
        print_hex_recursive(n / 16, uppercase);

    /* escreve o resto da divisão*/
    write(1, &base[n % 16], 1);
}
/*
Imprime o número 'n' em hexadecimal e devolve
 Retorna quantidade de dígitos (número de caracteres impressos).
*/
int ft_puthex(unsigned int n, int uppercase)
{
    if (n == 0)
        write(1, "0", 1);
    else
        print_hex_recursive(n, uppercase);
    return (count_hex_digits(n));
}
