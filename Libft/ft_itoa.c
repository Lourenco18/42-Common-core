/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 11:27:25 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/17 11:30:00 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

static int num_len(long n)
{
    int len = (n <= 0);
    while (n)
    {
        n /= 10;
        len++;
    }
    return (len);
}

char *ft_itoa(int n)
{
    long num = n;
    int len = num_len(num);
    char *str = malloc(len + 1);

    if (!str)
        return (0);
    str[len--] = '\0';
    if (num == 0)
        str[0] = '0';
    if (num < 0)
    {
        str[0] = '-';
        num = -num;
    }
    while (num)
    {
        str[len--] = (num % 10) + '0';
        num /= 10;
    }
    return (str);
}
