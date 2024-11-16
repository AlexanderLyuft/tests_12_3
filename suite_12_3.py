            # Домашнее задание по теме "Систематизация и пропуск тестов".


import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создание тестового набора
rts = unittest.TestSuite()

# Добавление тестов из классов RunnerTest и TournamentTest
rts.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
rts.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Запуск тестов с заданным уровнем подробности
runner = unittest.TextTestRunner(verbosity=2)
runner.run(rts)



