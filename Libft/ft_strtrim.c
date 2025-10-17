/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 11:26:00 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/17 11:30:12 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int is_in_set(char c, char const *set)
{
    while (*set)
        if (c == *set++)
            return (1);
    return (0);
}

char *ft_strtrim(char const *s1, char const *set)
{
    int start;
    int end;

    if (!s1 || !set)
        return (0);
    start = 0;
    while (s1[start] && is_in_set(s1[start], set))
        start++;
    end = ft_strlen(s1);
    while (end > start && is_in_set(s1[end - 1], set))
        end--;
    return (ft_substr(s1, start, end - start));
}
