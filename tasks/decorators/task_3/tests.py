import unittest

from tasks.common import some_func
from tasks.decorators.task_3.implementation import counter


class MyTestCase(unittest.TestCase):

    def test_on_number_calling_times(self):
        new_some_func = counter(some_func)
        new_some_func()
        new_some_func()
        new_some_func()
        new_some_func()
        self.assertEqual(new_some_func(), 5)


if __name__ == '__main__':
    unittest.main()
