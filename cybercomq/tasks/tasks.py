from celery.task import task
import random

#Default base directory 
#basedir="/data/static/"


#Example task
@task()
def add(x, y):
    """ Example task that adds two numbers or strings
        args: x and y
        return addition or concatination of strings
    """
    result = x + y
    return result

@task()
def randm_number(seed):
    """
       It generates a random number based of a given seed value
       args:
           seed
       return:
           random number
    """
    return random.random(seed)

