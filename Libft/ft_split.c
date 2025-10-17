/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 11:26:46 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/17 11:30:00 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

static int word_count(char const *s, char c)
{
    int count = 0;
    while (*s)
    {
        while (*s && *s == c)
            s++;
        if (*s)
            count++;
        while (*s && *s != c)
            s++;
    }
    return (count);
}

static char *word_dup(const char *s, int start, int end)
{
    char *word = malloc(end - start + 1);
    int i = 0;
    while (start < end)
        word[i++] = s[start++];
    word[i] = '\0';
    return (word);
}

char **ft_split(char const *s, char c)
{
    char **result;
    int i = 0, j = 0, index = -1;

    if (!s)
        return (0);
    result = malloc((word_count(s, c) + 1) * sizeof(char *));
    if (!result)
        return (0);
    while (s[i])
    {
        if (s[i] != c && index < 0)
            index = i;
        else if ((s[i] == c || s[i + 1] == '\0') && index >= 0)
        {
            result[j++] = word_dup(s, index, (s[i] == c) ? i : i + 1);
            index = -1;
        }
        i++;
    }
    result[j] = 0;
    return (result);
}
