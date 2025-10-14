/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 11:38:31 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/14 12:01:52 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
int ft_strlen(char *s)
{
    int size;

    size = 0;
    while (s[size])
    {
        size++;
    }
    return (size);
}
/*
int main(){

    printf("%d", ft_strlen("123"));
}
    */