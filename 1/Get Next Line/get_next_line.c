/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dasantos <dasantos@student.42porto.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 09:31:07 by dasantos          #+#    #+#             */
/*   Updated: 2025/10/28 10:21:08 by dasantos         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
/*
1-read the file, line by line
2-return the line with the \n included
3-if end or any error return NULL*/
char *get_next_line(int fd)
{
    char *line = malloc(256); // alocar memoria para a linha
    if (!line)
        return NULL;
    ssize_t bytes_read = read(fd, line, 255); // ler do file descriptor
    if (bytes_read <= 0)
    {
        free(line); // libertar memoria em caso de erro ou fim de ficheiro
        return NULL;
    }
    line[bytes_read] = '\0'; // adicionar o terminador de string
    return line;
}
int main()
{
    FILE *file = fopen("file.txt", "r"); // abrir ficheiro em modo leitura
    if (file)
    {
        int fd = fileno(file); // obter file descriptor
        char *line;
        while ((line = get_next_line(fd))) // enquanto houver linhas
        {
            printf("%s", line); // imprimir linha
            free(line);         // libertar memoria
        }
        fclose(file); // fechar ficheiro
        // fazer while linha a linha para a minha funcao principal
        return 0;
    }
}