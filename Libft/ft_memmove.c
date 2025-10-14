/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 14:26:02 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/14 14:37:28 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include <stdlib.h>
void *ft_memmove(void *dst, const void *src, size_t len)
{
    if (!dst && !src)
        return (NULL);
    unsigned char *d = (unsigned char *)dst;
    const unsigned char *s = (const unsigned char *)src;
    if (d == s)
        return (dst);
    if (d < (unsigned char *)s)
        for (size_t i = 0; i < len; i++)
            d[i] = s[i];
    else
        for (size_t i = len; i > 0; i--)
            d[i - 1] = s[i - 1];
    return (dst);
}