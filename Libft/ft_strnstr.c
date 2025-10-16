/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 12:08:08 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/16 12:32:10 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char *ft_strnstr(const char *haystack, const char *needle, unsigned int len)
{
    int i = 0;
    int j;

    if (!*needle)
        return (char *)haystack;

    while (haystack[i] && i < len)
    {
        j = 0;
        while (haystack[i + j] == needle[j] && (i + j) < len)
        {
            if (!needle[j + 1])
                return (char *)&haystack[i];
            j++;
        }
        i++;
    }
    return (0);
}
