/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 12:18:25 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/16 12:35:27 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void *ft_calloc(int nmemb, unsigned int size)
{
    void *ptr;
    if (nmemb && size && nmemb > SIZE_MAX / size)
        return (0);
    ptr = malloc(nmemb * size);
    if (!ptr)
        return (0);
    ft_bzero(ptr, nmemb * size);
    return ptr;
}
