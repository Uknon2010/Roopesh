a = []
a. append(1)
a.append(2)
print (a)

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes_from_2_to_100 = [i for i in range(2, 101) if is_prime(i)]
length = len(primes_from_2_to_100)
print(length)

primes_from_2_to_100 = [i for i in range(2, 101) if is_prime(i)]
print(primes_from_2_to_100)

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
print(list_of_lists[1][2])

print = len(list_of_lists[0])


class_names = ('rishabh', 'nandey', 'sanjana')

print(class_names)

print('simran' in class_names)
print('rishabh' in class_names)


date_of_birth = {}
date_of_birth["Siddarth"] = "31st Oct"
date_of_birth["Nandey"] = "22nd Jan"
date_of_birth["Atheendra"] = "20th Oct"


print('Nandey' in date_of_birth)
print('Simran' in date_of_birth)

print(date_of_birth["Atheendra"])
