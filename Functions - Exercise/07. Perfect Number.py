# receive integer
number = int(input())


# write a function if the number is perf or not
def is_number_perfect(num=number):
    is_perfect = False
    if num < 0:
        return "It's not so perfect."
    summary_of_divisors = 0
    for numbers in range(1, num):
        if num % numbers == 0:
            summary_of_divisors += numbers
    if summary_of_divisors == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(is_number_perfect())
