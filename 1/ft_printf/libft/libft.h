/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 11:01:41 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/22 12:18:28 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
#define LIBFT_H

#include <stdlib.h>
#include <unistd.h>

void ft_putnbr_fd(int n, int fd);
void ft_putstr_fd(char *s, int fd);
void ft_putchar_fd(char c, int fd);

#endif