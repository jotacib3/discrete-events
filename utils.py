import random
import math

def exponential(x):
    r = random.random()
    s = ( -1 / x ) * ( math.log(r , math.e ) )
    return s


def normal(mu, sigma):
    a = random.random()
    b = random.random()
    c = math.sqrt( -2 * math.log( a , math.e ) ) * math.cos( 2 * math.pi * b )
    return math.sqrt( sigma ) * math.fabs(c) + mu
