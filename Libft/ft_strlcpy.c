/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 14:30:26 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/17 11:09:08 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

unsigned int ft_strlcpy(char *dst, const char *src, int dstsize)
{
    int srclen = ft_strlen(src);
    if (dstsize == 0)
        return (srclen);
    int i;
    i = 0;
    while (i + 1 < dstsize && src[i])
    {
        dst[i] = src[i];
        i++;
    }
    dst[i] = '\0';
    return (srclen);
}