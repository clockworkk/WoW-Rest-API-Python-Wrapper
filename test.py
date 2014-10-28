from pywow import Realm

def test_prep():
	api = Realm("Bloodhoof")
	return api

def test_a():
	api = test_prep()
	test_a = api.get_realm_status()

	if(test_a == True or test_a == False):
		return "Test A: Pass - realm status: " + str(test_a)
	else:
		return "Test B: Failed"

def test_b():
	api = test_prep()
	test_b = api.get_realm_population()

	if(test_b != ""):
		return "Test B Passed - Realm Population: " + test_b
	else:
		return "Test B Failed with an error"

def test_c():
	api = test_prep()
	test_c = api.get_connected_realms()

	if not test_c:
		return "Has no connected realms or failed"
	else:
		return test_c


def main():
	first_test = test_a()
	print first_test

	second_test = test_b()
	print second_test

	third_test = test_c()
	print third_test
	
if __name__ == '__main__':
	main()

