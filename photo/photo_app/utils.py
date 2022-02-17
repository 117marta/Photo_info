# Helper functions


# A - photo, B - user
def get_centered_coordinates(latA, lonA, latB=None, lonB=None):
    coord = [latA, lonA]
    if latB and lonB:
        latB = float(latB)
        lonB = float(lonB)
        coord = [(latA + latB) / 2, (lonA + lonB) / 2]
    return coord


def get_zoom(dst):
    if dst <= 20:
        return 12
    elif dst > 20 and dst <= 50:
        return 11
    elif dst > 50 and dst <= 100:
        return 10
    elif dst > 100 and dst <= 1000:
        return 7
    elif dst > 1000 and dst <= 5000:
        return 4
    else:
        return 2
