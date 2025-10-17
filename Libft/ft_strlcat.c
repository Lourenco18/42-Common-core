/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 14:37:06 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/17 11:07:43 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

unsigned int ft_strlcat(char *dest, const char *src, int size)
{
    int i;
    int j;
    int dest_len;
    int src_len;

    dest_len = ft_strlen(dest);
    src_len = ft_strlen(src);
    if (size <= dest_len)
    {
        return (size + src_len);
    }
    i = dest_len;
    j = 0;
    while (src[j] && i + 1 < size)
    {
        dest[i] = src[j];
        i++;
        j++;
    }
    dest[i] = '\0';
    return (dest_len + src_len);
}