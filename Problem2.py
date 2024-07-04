def square_evens(numbers:list):
    return[num**2 for num in numbers if num % 2 ==0]

numbers = [1,4,7,8,9,12,15]
print(square_evens(numbers))