/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 13:26:48 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/17 11:02:37 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
void *ft_memcpy(void *dst, const void *src, int n)
{
    if (!dst && !src)
        return ((0));
    unsigned char *d = (unsigned char *)dst;
    const unsigned char *s = (const unsigned char *)src;
    for (int i = 0; i < n; i++)
        d[i] = s[i];
    return (dst);
}