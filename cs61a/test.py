import math
def nearest_two(num):
	ceil_num = math.ceil(math.log(num,2))
	floor_num = math.floor(math.log(num,2))
	if (pow(2,ceil_num)-num) > (num-pow(2,floor_num)):
		power_of_two = pow(2,floor_num)
	else:
		power_of_two = pow(2,ceil_num)
	return power_of_two


