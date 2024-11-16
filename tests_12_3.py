            # Домашнее задание по теме "Систематизация и пропуск тестов".


import unittest

# Декоратор для пропуска тестов
def skip_if_frozen(is_frozen):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if is_frozen:
                raise unittest.SkipTest("Тесты в этом кейсе заморожены")
            return func(*args, **kwargs)
        return wrapper
    return decorator

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen(is_frozen)
    def test_challenge(self):
        # Ваш код теста
        self.assertTrue(True)

    @skip_if_frozen(is_frozen)
    def test_run(self):
        # Ваш код теста
        self.assertTrue(True)

    @skip_if_frozen(is_frozen)
    def test_walk(self):
        # Ваш код теста
        self.assertTrue(True)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen(is_frozen)
    def test_first_tournament(self):
        # Ваш код теста
        self.assertTrue(True)

    @skip_if_frozen(is_frozen)
    def test_second_tournament(self):
        # Ваш код теста
        self.assertTrue(True)

    @skip_if_frozen(is_frozen)
    def test_third_tournament(self):
        # Ваш код теста
        self.assertTrue(True)




