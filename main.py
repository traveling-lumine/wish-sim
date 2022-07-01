from multiprocessing import freeze_support

from src.option import wish_by_pickups, pickup_by_wishes, pickup_ge_bar_wish


def main():
    freeze_support()
    selector()


def selector():
    while True:
        string_input = input('Please choose the type of calculation:\n'
                             '1. Calculate the number of wishes by the number of pickups\n'
                             '2. Calculate the number of pickups by the number of wishes\n'
                             '3. Percentage of pickup number satisfied by wishes\n'
                             'q. Exit\n')
        if string_input == '1':
            wish_by_pickups_sel()
        elif string_input == '2':
            pickup_by_wishes_sel()
        elif string_input == '3':
            pickup_ge_bar_wish_sel()
        elif string_input == 'q':
            return


def wish_by_pickups_sel():
    pickups = get_pickups()
    ip, ig = get_ip_ig()
    mean, maxi, mini = wish_by_pickups(pickups, ip, ig)
    print(f'The mean number of wishes is {mean}, '
          f'the max number of wishes is {maxi}, '
          f'the min number of wishes is {mini}')


def pickup_by_wishes_sel():
    wishes = get_wishes()
    ip, ig = get_ip_ig()
    mean, maxi, mini = pickup_by_wishes(wishes, ip, ig)
    print(f'The mean number of pickups is {mean}, '
          f'the max number of pickups is {maxi}, '
          f'the min number of pickups is {mini}')


def pickup_ge_bar_wish_sel():
    pickups = get_pickups()
    wishes = get_wishes()
    ip, ig = get_ip_ig()
    prob, _, _ = pickup_ge_bar_wish(pickups, wishes, ip, ig)
    print(f'The probability of pickup number satisfied by wishes is {prob}')


def get_wishes():
    wishes = None
    while wishes is None:
        try:
            wishes = int(input('Please input the number of wishes: '))
        except ValueError:
            print('Please input a valid number.')
    return wishes


def get_pickups():
    pickups = None
    while pickups is None:
        try:
            pickups = int(input('Please input the number of pickups: '))
        except ValueError:
            print('Please input a valid number.')
    return pickups


def get_ip_ig():
    ip = None
    while ip is None:
        try:
            ip = int(input('Please input the number of initial pity: '))
        except ValueError:
            print('Please input a valid number.')
    ig = None
    while ig is None:
        try:
            ig = int(input('Please input the guarantee state: '))
        except ValueError:
            print('Please input a valid number.')
    return ip, ig


if __name__ == '__main__':
    main()
