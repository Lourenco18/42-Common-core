/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 14:37:06 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/14 14:37:29 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
size_t ft_strlcat(char *dst, const char *src, size_t dstsize)
{
    size_t dstlen = 0;
    while (dstlen < dstsize && dst[dstlen])
        dstlen++;
    size_t srclen = ft_strlen(src);
    if (dstlen == dstsize)
        return (dstsize + srclen);
    size_t i = 0;
    while (dstlen + i + 1 < dstsize && src[i])
    {
        dst[dstlen + i] = src[i];
        i++;
    }
    if (dstlen + i < dstsize)
        dst[dstlen + i] = '\0';
    return (dstlen + srclen);
}