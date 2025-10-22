/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 12:06:21 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/22 12:18:34 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
#define FT_PRINTF_H
#include "libft/libft.h" // usar libft
#include <stdlib.h>
#include <unistd.h>
#include <stdarg.h> // number variable de argumentos
int ft_printf(const char *format, ...);
int ft_puthex(unsigned int n, const char format);
int ft_putptr(void *ptr);
int ft_putunbr(unsigned int n);

#endif