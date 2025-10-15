/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 12:19:01 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/15 12:22:23 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
char *ft_strdup(const char *s1)
{
    size_t len = ft_strlen(s1);
    char *dup = malloc(len + 1);
    if (!dup)
        return NULL;
    for (size_t i = 0; i < len; i++)
        dup[i] = s1[i];
    dup[len] = '\0';
    return dup;
}
