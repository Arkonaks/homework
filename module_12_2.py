import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name if isinstance(other, Runner) else self.name == other


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)
                    break
        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    def test_usain_nik_race(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertEqual(result[max(result.keys())], self.runner_3)

    def test_andrey_nik_race(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertEqual(result[max(result.keys())], self.runner_3)

    def test_usain_andrey_nik_race(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertEqual(result[max(result.keys())], self.runner_3)


if __name__ == "__main__":
    unittest.main()
