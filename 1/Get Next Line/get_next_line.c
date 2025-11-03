/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 09:31:07 by dasantos          #+#    #+#             */
/*   Updated: 2025/11/02 18:28:39 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char *get_next_line(int fd)
{
    char *line = malloc(256);
    if (!line)
        return (NULL);
    ssize_t bytes_read = read(fd, line, 255);
    if (bytes_read <= 0)
    {
        free(line);
        return (NULL);
    }
    line[bytes_read] = '\0';
    return (line);
}
int main(void)
{
    FILE *file = fopen("file.txt", "r");
    if (file)
    {
        int fd = fileno(file);
        char *line;
        while ((line = get_next_line(fd)))
        {
            printf("%s", line);
            free(line);
        }
        fclose(file);

        return (0);
    }
}