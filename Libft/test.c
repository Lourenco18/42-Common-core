#include "libft.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Função auxiliar para ft_strmapi
static char add_index(unsigned int i, char c)
{
    return (c + i);
}

// Função auxiliar para ft_striteri
static void modify_char(unsigned int i, char *c)
{
    *c = *c + i;
}

int main(void)
{

    // Verification functions
    printf("ft_isalpha('a') = %d\n", ft_isalpha('a'));
    printf("ft_isdigit('5') = %d\n", ft_isdigit('5'));
    printf("ft_isalnum('z') = %d\n", ft_isalnum('z'));
    printf("ft_isascii(128) = %d\n", ft_isascii(128));
    printf("ft_isprint('\\n') = %d\n", ft_isprint('\n'));

    // Memory functions
    char buffer[20];
    ft_memset(buffer, 'A', 10);
    buffer[10] = '\0';
    printf("ft_memset: %s\n", buffer);

    ft_bzero(buffer, 10);
    printf("ft_bzero: ");
    for (int i = 0; i < 10; i++)
        printf("%d ", buffer[i]);
    printf("\n");

    char src[] = "Hello";
    char dst[10];
    ft_memcpy(dst, src, 6);
    printf("ft_memcpy: %s\n", dst);

    char overlap[] = "Overlap";
    ft_memmove(overlap + 2, overlap, 5);
    overlap[7] = '\0';
    printf("ft_memmove: %s\n", overlap);

    void *ptr = ft_calloc(5, sizeof(int));
    int *arr = (int *)ptr;
    printf("ft_calloc: ");
    for (int i = 0; i < 5; i++)
        printf("%d ", arr[i]);
    printf("\n");
    free(ptr);

    char mem[] = "abcdef";
    char *found = ft_memchr(mem, 'c', 6);
    printf("ft_memchr: %c\n", found ? *found : '?');
    printf("ft_memcmp: %d\n", ft_memcmp("abc", "abd", 3));

    // String functions
    printf("ft_strlen: %u\n", ft_strlen("Hello World"));

    char lcpy_dst[20];
    ft_strlcpy(lcpy_dst, "Hello", 20);
    printf("ft_strlcpy: %s\n", lcpy_dst);

    char lcat_dst[20] = "Hi ";
    ft_strlcat(lcat_dst, "there", 20);
    printf("ft_strlcat: %s\n", lcat_dst);

    printf("ft_strncmp: %d\n", ft_strncmp("abc", "abd", 2));

    char *found_str = ft_strnstr("Hello World", "World", 11);
    printf("ft_strnstr: %s\n", found_str ? found_str : "NULL");

    char *dup = ft_strdup("Duplicate me");
    printf("ft_strdup: %s\n", dup);
    free(dup);

    printf("ft_strchr: %s\n", ft_strchr("Hello", 'e'));
    printf("ft_strrchr: %s\n", ft_strrchr("Hello", 'l'));

    // Conversion functions
    printf("ft_toupper('a') = %c\n", ft_toupper('a'));
    printf("ft_tolower('A') = %c\n", ft_tolower('A'));
    printf("ft_atoi('  -123abc') = %d\n", ft_atoi("  -123abc"));

    printf("\n=============================================\n");
    printf("🧠 LIBFT TEST — PART 2\n");
    printf("=============================================\n");

    // ft_substr
    char *sub = ft_substr("HelloWorld", 2, 5);
    printf("ft_substr(\"HelloWorld\", 2, 5): %s\n", sub);
    free(sub);

    // ft_strjoin
    char *join = ft_strjoin("Hello", "42");
    printf("ft_strjoin(\"Hello\", \"42\"): %s\n", join);
    free(join);

    // ft_strtrim
    char *trim = ft_strtrim("...Hello...", ".");
    printf("ft_strtrim(\"...Hello...\", \".\"): %s\n", trim);
    free(trim);

    // ft_split
    char **split = ft_split("one,two,three", ',');
    printf("ft_split(\"one,two,three\", ','):\n");
    for (int i = 0; split[i]; i++)
    {
        printf("  [%d] %s\n", i, split[i]);
        free(split[i]);
    }
    free(split);

    // ft_itoa
    char *itoa_res = ft_itoa(-12345);
    printf("ft_itoa(-12345): %s\n", itoa_res);
    free(itoa_res);

    // ft_strmapi
    char *mapped = ft_strmapi("abcd", add_index);
    printf("ft_strmapi(\"abcd\", add_index): %s\n", mapped);
    free(mapped);

    // ft_striteri
    char test_iteri[] = "abcd";
    ft_striteri(test_iteri, modify_char);
    printf("ft_striteri(\"abcd\", modify_char): %s\n", test_iteri);

    // Output functions (fd)
    printf("\nTesting ft_putchar_fd, ft_putstr_fd, ft_putendl_fd, ft_putnbr_fd:\n");
    ft_putchar_fd('A', 1);
    write(1, "\n", 1);
    ft_putstr_fd("Hello", 1);
    write(1, "\n", 1);
    ft_putendl_fd("World", 1);
    ft_putnbr_fd(12345, 1);
    write(1, "\n", 1);

    printf("\n✅ All tests completed!\n");
    return (0);
}
