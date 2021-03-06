import sys
sys.path.append("/Users/clockwork/Github/pywow")
from pywow import pywow

def test_prep():
	api = pywow.Realm("Bloodhoof")
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
	test_d = api.get_battlegroup()

	if (test_d != ""):
		return "Test D has passed: Battlegroup: " + test_d
	else:
		return "Test D has failed"

def test_e():
	api = test_prep()
	test_e = api.get_timezone()

	if (test_e != ""):
		return "Test D has passed: Timezone: " + test_e
	else:
		return "Test D has failed"

def test_f():
	api = test_prep()
	test_f = api.get_tb_data()

	return test_f

def test_g():
	pass

def test_h():
	pass

def test_i():
	pass

def test_j():
	pass


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

	sixth_test = test_f()


if __name__ == '__main__':
	main()

