import unittest


loader = unittest.TestLoader()
tests = unittest.TestSuite(loader.discover('.'))
unittest.TextTestRunner(verbosity=2).run(tests)