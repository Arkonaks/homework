import unittest
import tests_12_1
import tests_12_3

tests = unittest.TestSuite()
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tests)
