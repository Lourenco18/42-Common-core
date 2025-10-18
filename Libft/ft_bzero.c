/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 12:04:32 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/18 15:20:14 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
// preencher toda a memória com '0'
void ft_bzero(void *s, unsigned int n)
{
    ft_memset(s, 0, n);
}