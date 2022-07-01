from random import random


class CharacterWish:
    def __init__(self, init_pity, init_guaranteed):
        self.chance = 0.6e-2
        self.pity = init_pity
        self.guaranteed = init_guaranteed

    def get_once(self):
        if self._get_chance():
            self.pity = 0
            if self.guaranteed or random() < 0.5:
                self.guaranteed = False
                return True
            else:
                self.guaranteed = True
                return False
        self.pity += 1
        return False

    def _get_chance(self):
        prob = self.chance + self.chance * 10 * max(0, self.pity - 72)
        return random() <= prob
