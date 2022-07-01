from multiprocessing import freeze_support

from src.model import CharacterWish
from src.runner import runner_wrapper


def worker(args):
    wishes, ip, ig = args
    wisher = CharacterWish(ip, ig)
    pickup_acc = 0
    wishes_acc = 0
    while wishes_acc < wishes:
        wishes_acc += 1
        pickup_acc += wisher.get_once()
    return pickup_acc


pickup_by_wishes = runner_wrapper(worker)


def main():
    freeze_support()
    print(pickup_by_wishes(93))


if __name__ == '__main__':
    main()
