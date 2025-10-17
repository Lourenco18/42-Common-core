/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 12:18:25 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/17 11:33:11 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

void *ft_calloc(unsigned int nmemb, unsigned int size)
{
    void *ptr;

    if (nmemb && size && nmemb > 4294967295U / size)
        return (0);
    ptr = malloc(nmemb * size);
    if (!ptr)
        return (0);
    ft_bzero(ptr, nmemb * size);
    return (ptr);
}
