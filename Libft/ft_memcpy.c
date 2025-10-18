/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 13:26:48 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/18 18:16:56 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// copiar n bytes da area de memoria src para a area de memoria dst
void *ft_memcpy(void *dst, const void *src, int n)
{
    if (!dst && !src) // caso ambos sejam NULL
        return (0);
    unsigned char *d = (unsigned char *)dst;
    const unsigned char *s = (const unsigned char *)src;
    for (int i = 0; i < n; i++)
        d[i] = s[i];
    return (dst);
}