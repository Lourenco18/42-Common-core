#include "ft_printf.h"

static int ft_puthex_ptr(unsigned long n)
{
	int count;
	char *base;

	count = 0;
	base = "0123456789abcdef";
	if (n >= 16)
		count += ft_puthex_ptr(n / 16);
	count += ft_putchar(base[n % 16]);
	return (count);
}

int ft_putptr(void *ptr)
{
	unsigned long address;
	int count;

	count = 0;
	if (!ptr)
		return (ft_putstr("(nil)"));
	address = (unsigned long)ptr;
	count += ft_putstr("0x");
	count += ft_puthex_ptr(address);
	return (count);
}
