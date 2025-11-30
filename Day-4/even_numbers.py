# Practice 3: The Filter (List + Function)
# Goal: Write a function get_even_numbers(numbers_list) that takes a list of numbers and returns a new list containing only the even ones.
# Test: Pass [1, 2, 3, 4, 5, 6] and make sure it returns [2, 4, 6].

def get_even_numbers(numbers_list):
        return [lists for lists in numbers_list if lists%2==0]
even_one=get_even_numbers([1, 2, 3, 4, 5, 6])
print(f"even nums: {even_one}")
