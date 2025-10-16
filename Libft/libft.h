/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 11:25:27 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/16 12:36:56 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

//Verification functions
int ft_isalpha(int c); // done
int ft_isdigit(int c); // done
int ft_isalnum(int c); // done
int ft_isascii(int c); // done
int ft_isprint(int c); // done


// memory functions
void *ft_memset(void *b, int c, unsigned int len);//done
void ft_bzero(void *s, unsigned int n);// done
void *ft_memcpy(void *dst, const void *src, unsigned int n);// done
void *ft_memmove(void *dst, const void *src, unsigned int len);// done
void *ft_calloc(unsigned int nmemb, unsigned int size);// done
void *ft_memchr(const void *s, int c, unsigned int n);// done 
int ft_memcmp(const void *s1, const void *s2, unsigned int n);


//string functions
unsigned int ft_strlen(const char *s);// done 
unsigned int ft_strlcpy(char *dst, const char *src, unsigned int dstsize);// done 
unsigned int ft_strlcat(char *dst, const char *src, unsigned int dstsize);// done 
int ft_strncmp(const char *s1, const char *s2, unsigned int n);// done 
char *ft_strnstr(const char *haystack, const char *needle, unsigned int len);// done 
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