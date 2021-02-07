import os
import unittest

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_blog_case')
    suite = unittest.defaultTestLoader.discover(path, pattern='test*.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)
