NAME = libft.a
CC = cc
CFLAGS = -Wall -Wextra -Werror
SRC = ft_*.c
OBJ = $(SRC:.c=.o)

$(NAME): $(OBJ)
	ar rcs $(NAME) $(OBJ)

all: $(NAME)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

bonus:
	$(MAKE) BONUS=1
