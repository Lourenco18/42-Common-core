/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 09:28:22 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/28 11:35:18 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
#define GET_NEXT_LINE_H

#include <stdlib.h>
#include <unistd.h>

#ifndef BUFFER_SIZE
#define BUFFER_SIZE 42
#endif

char *get_next_line(int fd);
size_t ft_strlen(char *s);
char *ft_strchr(char *s, int c);
char *ft_strjoin(char *s1, char *s2);
char *ft_extract_line(char *s);
char *ft_save_remainder(char *s);

#endif
