import random
import logging


TARGET_KARMA = 500

class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass


def one_day():
    if random.randint(1, 10) == 1:
        raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
    return random.randint(1, 7)


logging.basicConfig(filename='karma.log', level=logging.INFO, encoding='UTF-8')

def main():
    karma = 0
    while karma < TARGET_KARMA:
        try:
            karma += one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
            logging.info(f'Исключение: {e.__class__.__name__}')
    print(f'Набрано {karma} очков кармы.')

if __name__ == "__main__":
    main()