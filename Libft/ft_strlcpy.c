/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 14:30:26 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/14 14:37:21 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

size_t ft_strlcpy(char *dst, const char *src, size_t dstsize)
{
    size_t srclen = ft_strlen(src);
    if (dstsize == 0)
        return (srclen);
    size_t i = 0;
    while (i + 1 < dstsize && src[i])
    {
        dst[i] = src[i];
        i++;
    }
    dst[i] = '\0';
    return (srclen);
}