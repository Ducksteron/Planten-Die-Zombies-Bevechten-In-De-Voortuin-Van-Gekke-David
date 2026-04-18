
def increase_sun(delta_time:float, sunwallet: SunWallet):
    sun_per_second:float = 50.0
    sunwallet.amount_of_sun += delta_time * sun_per_second
    sunwallet.total_sun_gotten += delta_time * sun_per_second



class SunWallet():
    amount_of_sun: float = 0.0
    total_sun_gotten: float = 0.0

