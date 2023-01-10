from models import *
import random

for apartment_id in range(1, 10):
    for year in (2017, 2018, 2019):
        s = InitialSaldo()

        s.apartment_id = apartment_id
        s.value = random.uniform(0, 20000)
        s.year = year

for apartment_id in range(1, 10):
    for year in (2017, 2018, 2019):
        for month in range(1, 12+1):
            p = Payment()
            p.apartment_id = apartment_id
            p.value = random.uniform(0, 20000)
            p.year = year
            p.month = month

            p.save()

            c = Charge()
            c.apartment_id = apartment_id
            c.value = random.uniform(0, 20000)
            c.year = year
            c.month = month

            c.save()
