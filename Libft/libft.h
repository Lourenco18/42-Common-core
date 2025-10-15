/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 11:25:27 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/14 18:51:02 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H


# include <stddef.h>
# include <stdlib.h>
//Verification functions
int ft_isalpha(int c); // done
int ft_isdigit(int c); // done
int ft_isalnum(int c); // done
int ft_isascii(int c); // done
int ft_isprint(int c); // done


// memory functions
void *ft_memset(void *b, int c, size_t len);// done
void ft_bzero(void *s, size_t n); // done
void *ft_memcpy(void *dst, const void *src, size_t n);//done 
void *ft_memmove(void *dst, const void *src, size_t len);//done
void *ft_calloc(size_t nmemb, size_t size);
void *ft_memchr(const void *s, int c, size_t n);
int ft_memcmp(const void *s1, const void *s2, size_t n);

//string functions
size_t ft_strlen(const char *s);// done
size_t ft_strlcpy(char *dst, const char *src, size_t dstsize);// done
size_t ft_strlcat(char *dst, const char *src, size_t dstsize); //done
char *ft_strchr(const char *s, int c);
char *ft_strrchr(const char *s, int c);
int ft_strncmp(const char *s1, const char *s2, size_t n);
char *ft_strnstr(const char *haystack, const char *needle, size_t len);
char *ft_strdup(const char *s1);

// to.. functions
int ft_toupper(int c);//done
int ft_tolower(int c);// done 
// transform functions
int ft_atoi(const char *str);




#endif