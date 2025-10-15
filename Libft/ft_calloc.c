/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 12:18:25 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/15 12:18:32 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
void *ft_calloc(size_t nmemb, size_t size)
{
    void *ptr;
    if (nmemb && size && nmemb > SIZE_MAX / size)
        return NULL;
    ptr = malloc(nmemb * size);
    if (!ptr)
        return NULL;
    ft_bzero(ptr, nmemb * size);
    return ptr;
}
