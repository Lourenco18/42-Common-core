NAME = libft.a
CC = gcc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs


SRCS = ft_is.c ft_string.c ft_memory.c ft_to.c ft_atoi.c ft_strl.c
OBJS = $(SRCS:.c=.o)


all: $(NAME)


$(NAME): $(OBJS)
$(AR) $(NAME) $(OBJS)


%.o: %.c libft.h
$(CC) $(CFLAGS) -c $< -o $@


clean:
rm -f $(OBJS)


fclean: clean
rm -f $(NAME)


re: fclean all