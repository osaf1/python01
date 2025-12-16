# Opdracht 1 functies
# Naam student:
# Groep:

import math

def rechthoek_oppervlakte(lengte, breedte):
    return lengte * breedte

def bol_vol(r):
    return (4/3) * math.pi * (r ** 3)

lengte = 4
breedte = 5
radius = 4

print(rechthoek_oppervlakte(lengte, breedte))
print(bol_vol(radius))
