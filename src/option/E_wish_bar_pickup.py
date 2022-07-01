from multiprocessing import freeze_support

from src.model import CharacterWish
from src.runner import int_type_runner


def worker(pickups):
    wisher = CharacterWish()
    pickup_acc = 0
    wishes_acc = 0
    while pickup_acc < pickups:
        wishes_acc += 1
        pickup_acc += wisher.get_once()
    return wishes_acc


wish_by_pickups = int_type_runner(worker)


def main():
    freeze_support()
    print(wish_by_pickups(1))


if __name__ == '__main__':
    main()
