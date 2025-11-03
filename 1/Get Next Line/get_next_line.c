/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 09:31:07 by dasantos          #+#    #+#             */
/*   Updated: 2025/11/03 11:08:04 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char *get_next_line(int fd)
{
    char *line = malloc(BUFFER_SIZE + 1);
    if (!line)
        return (NULL);
    ssize_t bytes_read = read(fd, line, BUFFER_SIZE);
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