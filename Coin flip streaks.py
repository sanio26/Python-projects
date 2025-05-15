print("Sanio Frederic,1AY24AI099,SEC-O")
import random

number_of_streaks = 0
num_experiments = 10000

for experiment_number in range(num_experiments):
    # Create a list of 100 'coin flips'
    flips = []
    for i in range(100):
        flips.append(random.choice(['H', 'T']))

    # Check for streaks of 6
    streak = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            streak += 1
            if streak == 6:
                number_of_streaks += 1
                break  # Only count one streak per trial
        else:
            streak = 1

print(f'Chance of a streak of 6 in 100 flips: {number_of_streaks / num_experiments * 100:.2f}%')
