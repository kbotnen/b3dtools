import random

def b3d_print(message):
    print(message)


def b3d_dicethrow(throws):
    result_array = []
    
    for i in range(0, throws):
        dice_throws = random.randrange(1,7)
        result_array.append(dice_throws)

    return result_array
