from BDviz.helper_functions import get_angular_separation, get_physical_separation
from BDviz.plotbd import BrownDwarf
import astropy.units as u

def test_ang_sep_known():
    bd1 = BrownDwarf("BD-1", ra=150, dec=20, distance=5, color='purple')
    bd2 = BrownDwarf("BD-2", ra=150, dec=25, distance=5, color='purple')

    result = get_angular_separation(bd1, bd2)
    assert result.unit == u.deg

    # Because RA is the same, angular separation = |dec1 - dec2| = 5 deg
    assert abs(result.value - 5.0) < 1e-5

def test_ang_sep_zero():
    bd1 = BrownDwarf("BD-1", ra=150, dec=20, distance=5, color='purple')
    result = get_angular_separation(bd1, bd1)

    assert result.value == 0

# if __name__ == "__main__":
#     test_ang_sep_known()
#     test_ang_sep_zero()