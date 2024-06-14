import random
import time

def waiting_game():
    target_time = random.randint(2, 15)
    print(f"Your target time is {target_time} seconds.")
    input("Press Enter to start the game.")
    start_time = time.time()
    input("Press Enter again after {} seconds.".format(target_time))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time: {:.3f} seconds".format(elapsed_time))
    if elapsed_time == target_time:
        print("Right on time!")
    elif elapsed_time < target_time:
        print("You were {:.3f} seconds too early.".format(target_time - elapsed_time))
    else:
        print("You were {:.3f} seconds too late.".format(elapsed_time - target_time))

waiting_game()