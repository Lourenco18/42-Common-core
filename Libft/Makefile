NAME = libft.a
CC = gcc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs

SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)

TEST = test
TEST_SRC = test.c
TEST_OBJ = $(TEST_SRC:.c=.o)

# -------------------
# Targets
# -------------------

all: $(NAME)

$(NAME): $(OBJ)
	$(AR) $@ $^

%.o: %.c libft.h
	$(CC) $(CFLAGS) -c $< -o $@

test: $(NAME) $(TEST_OBJ)
	$(CC) $(CFLAGS) $(TEST_OBJ) -L. -lft -o $(TEST)

clean:
	rm -f $(OBJ) $(TEST_OBJ)

fclean: clean
	rm -f $(NAME) $(TEST)

re: fclean all

.PHONY: all clean fclean re test
