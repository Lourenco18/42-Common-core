/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 10:33:29 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/28 11:06:14 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t ft_strlen(char *s)
{
    size_t i;

    i = 0;
    while (s && s[i])
        i++;
    return (i);
}

char *ft_strchr(char *s, int c)
{
    if (!s)
        return (NULL);
    while (*s)
    {
        if (*s == (char)c)
            return ((char *)s);
        s++;
    }
    return (NULL);
}

char *ft_strjoin(char *s1, char *s2)
{
    size_t len1;
    size_t len2;
    char *res;
    size_t i;

    len1 = ft_strlen(s1);
    len2 = ft_strlen(s2);
    res = malloc(len1 + len2 + 1);
    i = 0;
    if (!res)
        return (NULL);
    while (s1 && s1[i])
    {
        res[i] = s1[i];
        i++;
    }
    for (size_t j = 0; s2 && s2[j]; j++)
        res[i++] = s2[j];
    res[i] = '\0';
    free(s1);
    return (res);
}

char *ft_extract_line(char *s)
{
    int i;
    char *line;
    size_t len;

    i = 0;
    if (!s || !s[0])
        return (NULL);
    while (s[i] && s[i] != '\n')
        i++;
    len = ft_strlen(s);
    line = malloc(len + 1);
    if (!line)
        return (NULL);
    while (s[i] && i < len)
    {
        line[i] = s[i];
        i++;
    }
    line[len] = '\0';
    return (line);
}

char *ft_save_remainder(char *s)
{
    int i;
    size_t len;
    char *new_s;

    i = 0;
    len = ft_strlen(s);
    if (!s || !s[len])
    {
        free(s);
        return (NULL);
    }
    len++;
    new_s = malloc(ft_strlen(s + len) + 1);
    if (!new_s)
        return (NULL);
    while (s[len])
        new_s[i++] = s[len++];
    new_s[i] = '\0';
    free(s);
    return (new_s);
}
