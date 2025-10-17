/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 11:28:57 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/17 11:30:22 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

static void put_char(char c, int fd)
{
    write(fd, &c, 1);
}

void ft_putnbr_fd(int n, int fd)
{
    long num = n;
    if (num < 0)
    {
        put_char('-', fd);
        num = -num;
    }
    if (num >= 10)
        ft_putnbr_fd(num / 10, fd);
    put_char((num % 10) + '0', fd);
}
