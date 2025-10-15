/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 12:20:03 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/15 12:20:17 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
void *ft_memchr(const void *s, int c, size_t n)
{
    const unsigned char *p = (const unsigned char *)s;
    while (n--)
    {
        if (*p == (unsigned char)c)
            return (void *)p;
        p++;
    }
    return NULL;
}
