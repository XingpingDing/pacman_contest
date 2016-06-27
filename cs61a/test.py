def fun(function):
	if function == hello:
		print('is hello')

def hello():
	return 'hello'


if __name__ == "__main__":
	fun(hello)