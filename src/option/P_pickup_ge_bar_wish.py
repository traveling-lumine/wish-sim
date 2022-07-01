from multiprocessing import freeze_support

from src.model import CharacterWish
from src.runner import pair_int_type_runner


def worker(args):
    pickup_thresold, wishes = args
    wisher = CharacterWish()
    pickup_acc = 0
    wishes_acc = 0
    while wishes_acc < wishes:
        wishes_acc += 1
        pickup_acc += wisher.get_once()
    return pickup_acc >= pickup_thresold


pickup_ge_bar_wish = pair_int_type_runner(worker)


def main():
    freeze_support()
    print(pickup_ge_bar_wish(1, 93))


if __name__ == '__main__':
    main()
