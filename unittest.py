class prime_isTest(TestCase):
    """docstring for prime_isTest"""

    def test_object_type(self):
        obj = prime_is()
        self.assertEqual(True, type(obj) is prime_is,
                         msg='should be of type `primenumber`')

    def test_obj_instance(self):
        obj = PrimeChecker()
        self.assertIsInstance(obj,
                              PrimeChecker,
                              msg='should be an instance of `primenumber`')
    def test_if_positive(self):
        prime = prime_is('-3')
        self.assertEqual(True,
                         prime.prime_is(),
                         msg='Accepts only positive values')
    def test_if_it_is_an_integer(self):
        prime = prime_is("green")
        self.assertEqual(True,
                         prime.prime_is(),
                         msg = 'Accepts only integers')

    def test_is_prime_one(self):
        prime = prime_is('41')
        self.assertEqual(True,
                         prime.prime_is(),
                         msg='should return true for 41')

    def test_is_prime_two(self):
        prime = prime_is('101')
        self.assertEqual(True,
                         prime.prime_is(),
                         msg='should return true for 101')

    def test_is_prime_three(self):
        prime = prime_is('67')
        self.assertEqual(True,
                         prime.prime_is(),
                         msg='should return false for 68')

    def test_is_prime_four(self):
        prime = prime_is('0')
        prime = prime_is('1')
        self.assertEqual(True,
                         prime.prime_is(),
                         msg='The number is not accepted')

    def test_is_prime_five(self):
        prime = prime_is('')
        self.assertEqual(False,
                         prime.is_prime(),
                         msg='You have an empty string')
