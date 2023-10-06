import unittest
# def distance(x,y,x1,y1):
# 	return((x - x1) ** 2 + (y - y1) ** 2) ** (0.5)

# class TestDistance(unittest.TestCase):

# 	def test1(self):
# 		self.assertEqual(distance(1, 1, 1, 2), 1)

# 	def test1(self):
# 		self.assertEqual(distance(0, 0, 10, 0), 10)

def rigester(name, surnsme, value, data):
	user = {'name': name, 'surnsme': surnsme, "value": value}
	if user not in data:
		data.append(user)
		return True
	return False


class TestRegister(unittest.TestCase):

	def test_register_new_user(self):
		data=[]
		self.assertTrue(rigester("max", "smith",1,data))



	def test_register_new_user(self):
		data=[]
		rigester("max", "smith",1,data)
		self.assertFalse(rigester("max", "smith",1,data))

unittest.main()