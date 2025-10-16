/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 14:26:02 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/16 12:36:30 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
void *ft_memmove(void *dst, const void *src, unsigned int len)
{
    if (!dst && !src)
        return ((0));
    unsigned char *d = (unsigned char *)dst;
    const unsigned char *s = (const unsigned char *)src;
    if (d == s)
        return (dst);
    if (d < (unsigned char *)s)
        for (int i = 0; i < len; i++)
            d[i] = s[i];
    else
        for (int i = len; i > 0; i--)
            d[i - 1] = s[i - 1];
    return (dst);
}