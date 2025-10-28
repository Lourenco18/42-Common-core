/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 09:28:22 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/28 10:03:19 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <fcntl.h> //open function
# include <stdio.h>
# include <stdlib.h> //malloc, free
# include <unistd.h> //read function

char	*get_next_line(int fd);

#endif
