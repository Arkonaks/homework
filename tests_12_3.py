import unittest
from module_12_2 import Tournament, Runner

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_nik_race(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertEqual(result[max(result.keys())], self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_nik_race(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertEqual(result[max(result.keys())], self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_nik_race(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertEqual(result[max(result.keys())], self.runner_3)


if __name__ == "__main__":
    unittest.main()