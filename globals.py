from utils import *

def type_generator():
    r = random.random()
    if r <= 0.25:
        return 0
    if r <= 0.5:
        return 1
    return 2

def load_time_generator(type):
    if type == 0:
        return normal(9, 1) * 60

    if type == 1:
        return normal(12, 2) * 60

    return normal(18, 3) * 60

def ship_arrival_generator():
    return exponential(8) * 60

def tugboat_transfer_generator():
    return exponential(15)

def take_boat_to_dock_generator():
    return exponential(2) * 60

def take_boat_out_port_generator():
    return exponential(1) * 60