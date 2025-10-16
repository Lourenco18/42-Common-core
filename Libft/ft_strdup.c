/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 12:19:01 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/16 12:36:30 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char *ft_strdup(char *src)
{
    int i;
    int len;
    char *dup;

    len = 0;
    while (src[len])
    {
        len++;
    }
    dup = (char *)malloc(sizeof(char) * (len + 1));
    if (!dup)
        return ((0));
    i = 0;
    while (src[i])
    {
        dup[i] = src[i];
        i++;
    }
    dup[i] = '\0';
    return (dup);
}
