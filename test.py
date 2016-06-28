import numpy as np
prime_list = [2,3,5,7,11,13,17,19]

def divide_prime(x):
	prime_num = np.zeros((1,8))
	for index in range(0,len(prime_list)):
		while not x % prime_list[index]:
			prime_num[index] += 1
			x = x//prime_list[index]
		if x == 1:
			break
	return prime_num


if __name__ == '__main__':
	result = 1
	prime_sum = np.zeros((10,8))
	for num in range(11,21):
		prime_sum[num-11,:] = divide_prime(num)
	ind = prime_sum.argmax(axis=0)
	prime_max = prime_sum[ind, range(prime_sum.shape[1])]
	for index in range(0,len(prime_max)):
		result *= pow(prime_list[index],prime_max[index])
	print(result)
