# Uses python3
def max_pairwise_product (numbers):
    numbers.sort (reverse = True)
    max_product = numbers[0] * numbers[1] 
    return max_product

n_i = int(input())
input_numbers = [int(x) for x in input().split()]
print(max_pairwise_product(input_numbers))
