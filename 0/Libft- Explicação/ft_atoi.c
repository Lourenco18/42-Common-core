/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 12:14:43 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/22 09:08:38 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// converter ascii para int
int ft_atoi(char *str)
{
    int i;
    int sinal;
    int result;

    i = 0;
    sinal = 1;
    result = 0;
    // Ignorar caso seja um ' ' ou tabs - '\n' '\t'
    while (str[i] == ' ' || (str[i] >= 9 && str[i] <= 13))
    {
        i++;
    }
    // caso seja um sinal '+' ignoramos
    if (str[i] == '+' || str[i] == '-')
    {
        // se for '-' muda-se o valor do sinal para negativo
        if (str[i] == '-')
        {
            sinal = -sinal;
        }
        i++;
    }
    // quando for um númeo fazemos a operação para mostrar o digito como inteiro
    while (str[i] >= '0' && str[i] <= '9')
    {
        result = result * 10 + (str[i] - '0');
        i++;
    }
    // retorna-se o inteiro multiplicando pelo sinal
    return (result * sinal);
}
