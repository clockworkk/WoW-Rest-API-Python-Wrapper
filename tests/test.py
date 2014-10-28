from ..pywow import Realm

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
		return "Test C has passed: connected realms: " + str(test_c)

def test_d():
	api = test_prep()
	test_c = api.get_battlegroup()

	if (test_c != ""):
		return "Test D has passed: Battlegroup: " + test_c
	else:
		return "Test D has failed"

def test_e():
	api = test_prep()
	test_d = api.get_timezone()

	if (test_c != ""):
		return "Test D has passed: Timezone: " + test_d
	else:
		return "Test D has failed"


def main():
	first_test = test_a()
	print first_test

	second_test = test_b()
	print second_test

	third_test = test_c()
	print third_test

	fourth_test = test_d()
	print fourth_test

	fifth_test = test_e()
	print fifth_test

if __name__ == '__main__':
	main()

