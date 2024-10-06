import unittest


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


class Tournament:
    def __init__(self, distance):
        self.distance = distance

    def start(self, runners):
        results = {}
        for runner in runners:
            time = self.distance / runner.speed
            results[time] = runner.name
        return results


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", 10)
        self.runner_andrey = Runner("Андрей", 9)
        self.runner_nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("\nРезультаты всех тестов:")
        for time in sorted(cls.all_results.keys()):
            print(f"{cls.all_results[time]} - {time:.2f} секунд")

    def test_race_usain_nik(self):
        tournament = Tournament(90)
        results = tournament.start([self.runner_usain, self.runner_nik])
        self.all_results.update(results)

        # Проверяем, что Ник был последним
        last_time = max(results.keys())
        self.assertTrue(results[last_time] == "Ник")

    def test_race_andrey_nik(self):
        tournament = Tournament(90)
        results = tournament.start([self.runner_andrey, self.runner_nik])
        self.all_results.update(results)

        last_time = max(results.keys())
        self.assertTrue(results[last_time] == "Ник")

    def test_race_usain_andrey_nik(self):
        tournament = Tournament(90)
        results = tournament.start([self.runner_usain, self.runner_andrey, self.runner_nik])
        self.all_results.update(results)

        last_time = max(results.keys())
        self.assertTrue(results[last_time] == "Ник")


if __name__ == "__main__":
    unittest.main()
