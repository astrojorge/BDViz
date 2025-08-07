from BDviz.helper_functions import get_angular_separation, get_physical_separation
from BDviz.plotbd import BrownDwarf

def test_ang_sep():
    bd1 = BrownDwarf("BD-1", ra=150, dec=20, distance=5, color='purple')
    bd2 = BrownDwarf("BD-1", ra=150, dec=25, distance=5, color='purple')
    get_angular_separation(bd1, bd1)

# def test_ang_sep_known_value():
#     # Brown dwarfs with 5 degrees separation in declination
#     bd1 = BrownDwarf("BD-1", ra=150, dec=20, distance=5, color='purple')
#     bd2 = BrownDwarf("BD-2", ra=150, dec=25, distance=5, color='purple')

#     result = get_angular_separation(bd1, bd2)

#     # Assert it's an angle in degrees
#     assert result.unit == u.deg

#     # Because RA is the same, angular separation = |dec1 - dec2| = 5 deg
#     assert abs(result.value - 5.0) < 1e-5

# def test_ang_sep_zero():
#     bd1 = BrownDwarf("BD-1", ra=150, dec=20, distance=5, color='purple')
#     result = get_angular_separation(bd1, bd1)

#     assert result.value == 0

# if __name__ == "__main__":
#     # test_period_basis()
#     # test_semi_amp_basis()
#     # test_xyz_basis()
#     test_ang_sep()