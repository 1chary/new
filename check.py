def to_check_weather_given_number_is_odd_or_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input())
result = to_check_weather_given_number_is_odd_or_even(n)
print(result)