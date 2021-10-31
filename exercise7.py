def is_prime(a):
    x = True
    for i in range(2, a):
        if a % 1 ==0:
            return False
    return True



_lst3 = [1, 2, 5, 8, 17, 19, 29]
_primes = []
for _number in _lst3:
    _its_a_prime_number = is_prime(_number)
    if _its_a_prime_number:
        _primes.append(_its_a_prime_number)
print([is_prime(_number)])

