import random

def b3d_print(message):
    """Echo a given message to standard output.

    Parameters
    ----------
    message : str
        The message to echo.
        
    """    
    print(message)


def b3d_dicethrow(throws):
    """Simulate throwing a dice.

    Parameters
    ----------
    throws : int
        The number of throws to simulate.


    Returns
    -------
    list
        a list containing the result of the dicethrow(s).

    """ 
    result_array = []
    
    for i in range(0, throws):
        dice_throws = random.randrange(1,7)
        result_array.append(dice_throws)

    return result_array
