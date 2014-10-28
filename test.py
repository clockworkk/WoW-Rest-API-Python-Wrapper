from pywow import Pywow


def test_a():
	api = Pywow()
	test_a = api.get_realm_status('Bloodhoof')

	if(test_a == True or test_a == False):
		return "Test A: Pass - realm status: " + str(test_a)
	else:
		return "Test B: Failed"

def main():
	first_test = test_a()
	print first_test

if __name__ == '__main__':
	main()

