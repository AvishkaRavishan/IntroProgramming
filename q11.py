def sum_even_numbers(numbers):
  total=0
  for num in numbers:
    if num % 2 ==0:
      total += num
  return total

nums=[1,10,3,4,5,9]
print("ans:",sum_even_numbers(nums))
