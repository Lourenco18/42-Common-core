/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_puthex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 11:15:42 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/23 11:17:43 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static void	print_hex(unsigned int n, int maiuscula)
{
	const char	*base;

	/* Define a base hexadecimal dependendo se é maiúscula ou minúscula */
	base = maiuscula ? "0123456789ABCDEF" : "0123456789abcdef";
	if (n >= 16)
		print_hex(n / 16, maiuscula);
			/* Chamada recursiva para o próximo dígito */
	write(1, &base[n % 16], 1);      
		/* Imprime o dígito hexadecimal correspondente */
}
/* Conta quantos dígitos são necessários para imprimir o número em hexadecimal */
static size_t	count_digits(unsigned int n)
{
	size_t	count;

	count = 1;
	while (n >= 16)
	{
		n /= 16;
		count++;
	}
	return (count);
}
/* Imprime o número 'n' em hexadecimal e retorna a quantidade de caracteres impressos (FUNCAO PRINCIPAL) */
int	ft_puthex(unsigned int n, int maiuscula)
{
	if (n == 0)
		return (write(1, "0", 1));
	print_hex(n, maiuscula);
	return (count_digits(n));
}
