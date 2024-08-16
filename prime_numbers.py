

def is_prime(input_num):
    list_of_numbers_from_2_to_nmisone = list(range(2,input_num))
    print(f"list_of_numbers = {list_of_numbers_from_2_to_nmisone}")
    for num in list_of_numbers_from_2_to_nmisone:
        if input_num % num ==0:
            return False
    return True

if __name__=="__main__":
    print("This is for testing purpose")

    input_numbers = [2,3,4,5,6,7,8,9,10,11,12]
    for num in input_numbers:
        if is_prime(num):
            print(f" input number is {num}, It is a prime")
        else:
            print(f" input number is {num}, It is not a prime")


