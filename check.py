def get_the_fibonaci_series(n):
    if (n == 0 or n == 1):
        return n
    else:
        return get_the_fibonaci_series(n - 1) + get_the_fibonaci_series(n - 2)

def to_check_the_number_is_prime_or_not(n):
    count = 0
    for i in range(2,n+1):
        if n % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


n = 9
result = get_the_fibonaci_series(n)
prime_number = to_check_the_number_is_prime_or_not(n)
print(prime_number)