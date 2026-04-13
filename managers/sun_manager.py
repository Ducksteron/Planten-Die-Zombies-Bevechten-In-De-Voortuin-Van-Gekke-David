
def increase_sun(delta_time:float, sunwallet: SunWallet):
    sun_per_second:float = 5.0
    sunwallet.amount_of_sun += delta_time * sun_per_second



class SunWallet():
    amount_of_sun: float = 0.0

