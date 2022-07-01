from multiprocessing import freeze_support

from src.model import CharacterWish
from src.runner import runner_wrapper


def worker(args):
    pickups, ip, ig = args
    wisher = CharacterWish(ip, ig)
    pickup_acc = 0
    wishes_acc = 0
    while pickup_acc < pickups:
        wishes_acc += 1
        pickup_acc += wisher.get_once()
    return wishes_acc


wish_by_pickups = runner_wrapper(worker)


def main():
    freeze_support()
    print(wish_by_pickups(1))


if __name__ == '__main__':
    main()
