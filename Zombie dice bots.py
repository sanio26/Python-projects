print("Sanio Frederic,1AY24AI099,SEC-O")
import zombiedice
import random

# A bot that stops after one roll
class StopAfterOneRollBot(zombiedice.Player):
    def turn(self, game_state):
        self.roll()
        while True:
            dice_results = self.get_last_roll()
            if dice_results is None:
                return
            else:
                return  # Stop after the first roll

# A bot that randomly decides whether to continue
class RandomBot(zombiedice.Player):
    def turn(self, game_state):
        self.roll()
        while True:
            dice_results = self.get_last_roll()
            if dice_results is None:
                return
            brains = sum(1 for d in dice_results if d['color'] and d['value'] == 'brain')
            shotguns = sum(1 for d in dice_results if d['value'] == 'shotgun')
            if random.choice([True, False]) or shotguns >= 2:
                return
            else:
                self.roll()

# A bot that stops after 2 brains
class StopAtTwoBrainsBot(zombiedice.Player):
    def turn(self, game_state):
        brains = 0
        self.roll()
        while True:
            dice_results = self.get_last_roll()
            if dice_results is None:
                return
            brains += sum(1 for d in dice_results if d['value'] == 'brain')
            if brains >= 2:
                return
            else:
                self.roll()

# A bot that stops if it has 2 or more shotguns
class TwoShotgunBot(zombiedice.Player):
    def turn(self, game_state):
        shotguns = 0
        self.roll()
        while True:
            dice_results = self.get_last_roll()
            if dice_results is None:
                return
            shotguns += sum(1 for d in dice_results if d['value'] == 'shotgun')
            if shotguns >= 2:
                return
            else:
                self.roll()

# Add more bots or modify these strategies

zombiedice.runTournament(
    players=[
        StopAfterOneRollBot(name='Cautious Carl'),
        RandomBot(name='Lucky Larry'),
        StopAtTwoBrainsBot(name='Brainy Betty'),
        TwoShotgunBot(name='Twitchy Tina')
    ],
    numGames=1000
)
