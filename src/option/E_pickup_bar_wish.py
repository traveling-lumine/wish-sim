from multiprocessing import freeze_support

from src.model import CharacterWish
from src.runner import int_type_runner


def worker(wishes):
    wisher = CharacterWish()
    pickup_acc = 0
    wishes_acc = 0
    while wishes_acc < wishes:
        wishes_acc += 1
        pickup_acc += wisher.get_once()
    return pickup_acc


pickup_by_wishes = int_type_runner(worker)


def main():
    freeze_support()
    print(pickup_by_wishes(93))


if __name__ == '__main__':
    main()
