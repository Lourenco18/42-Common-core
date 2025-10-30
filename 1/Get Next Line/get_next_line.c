/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 11:39:08 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/30 11:48:43 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*join_and_free(char *s1, char *s2)
{
	char	*temp;

	temp = ft_strjoin(s1, s2);
	free(s1);
	return (temp);
}

static char	*read_and_stash(int fd, char *backup)
{
	char	*past;
	ssize_t	bytes_read;

	if (!backup)
		backup = ft_strdup("");
	past = malloc(BUFFER_SIZE + 1);
	if (!past)
		return (NULL);
	bytes_read = 1;
	while (!ft_strchr(backup, '\n') && bytes_read > 0)
	{
		bytes_read = read(fd, past, BUFFER_SIZE);
		if (bytes_read < 0)
			return (free(past), free(backup), NULL);
		past[bytes_read] = '\0';
		backup = join_and_free(backup, past);
		if (!backup)
			return (free(past), NULL);
	}
	free(past);
	return (backup);
}

static char	*save_remainder(char *stash)
{
	int		i;
	int		j;
	char	*remainder;

	i = 0;
	while (stash[i] && stash[i] != '\n')
		i++;
	if (!stash[i])
		return (free(stash), NULL);
	remainder = malloc(ft_strlen(stash) - i);
	if (!remainder)
		return (NULL);
	i++;
	j = 0;
	while (stash[i])
		remainder[j++] = stash[i++];
	remainder[j] = '\0';
	free(stash);
	return (remainder);
}

char	*get_next_line(int fd)
{
	static char	*backup;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0 || read(fd, 0, 0) < 0)
		return (NULL);
	backup = read_and_stash(fd, backup);
	if (!backup)
		return (NULL);
	line = extract_line(backup);
	backup = save_remainder(backup);
	if (!line || !*line)
	{
		free(backup);
		backup = NULL;
		if (line)
			free(line);
		return (NULL);
	}
	return (line);
}
