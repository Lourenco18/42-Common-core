/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 11:25:27 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/15 15:55:52 by dasantos         ###   ########.fr       */
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
void *ft_calloc(size_t nmemb, size_t size);// done
void *ft_memchr(const void *s, int c, size_t n);// done
int ft_memcmp(const void *s1, const void *s2, size_t n);// done

//string functions
size_t ft_strlen(const char *s);// done
size_t ft_strlcpy(char *dst, const char *src, size_t dstsize);// done
size_t ft_strlcat(char *dst, const char *src, size_t dstsize); //done
int ft_strncmp(const char *s1, const char *s2, size_t n);//done 
char *ft_strnstr(const char *haystack, const char *needle, size_t len); // done 
char *ft_strdup(const char *s1); // done

//Shearch functions
char *ft_strchr(const char *s, int c);// done
char *ft_strrchr(const char *s, int c);// done

// Conversion functions
int ft_toupper(int c);//done
int ft_tolower(int c);// done 
// transform functions
int ft_atoi(const char *str);// done




#endif