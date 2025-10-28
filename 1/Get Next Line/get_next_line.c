/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 09:31:07 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/28 11:01:35 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char *get_next_line(int fd)
{
    static char *remainder;
    char *buffer;
    char *line;
    ssize_t bytes;

    if (fd < 0 || BUFFER_SIZE <= 0)
        return (NULL);
    buffer = malloc(BUFFER_SIZE + 1);
    if (!buffer)
        return (NULL);
    bytes = 1;
    while (!ft_strchr(remainder, '\n') && bytes > 0) // loop until newline is found or EOF
    {
        bytes = read(fd, buffer, BUFFER_SIZE); // read from file descriptor
        if (bytes < 0)                         // check for read error
        {
            free(buffer);
            return (NULL);
        }
        buffer[bytes] = '\0';                      // null-terminate the buffer
        remainder = ft_strjoin(remainder, buffer); // join the strings
    }
    free(buffer);
    line = ft_extract_line(remainder);
    remainder = ft_save_remainder(remainder);
    return (line);
}

/*
int	main(void)
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
}*/