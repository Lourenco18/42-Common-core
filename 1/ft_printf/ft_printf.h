/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 12:40:00 by yourlogin         #+#    #+#             */
/*   Updated: 2025/10/22 12:35:14 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
#define FT_PRINTF_H

#include <stdarg.h>
#include <unistd.h>

int ft_putchar(char c);
int ft_putstr(char *s);
int ft_putnbr(int n);
int ft_printf(const char *fmt, ...);

int ft_putunbr(unsigned int n);
int ft_puthex(unsigned int n, const char format);
int ft_putptr(void *ptr);

#endif
