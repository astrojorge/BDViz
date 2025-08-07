from BDviz.helper_functions import get_angular_separation, get_physical_separation
from BDviz.plotbd import BrownDwarf

def test_ang_sep():
    bd1 = BrownDwarf("BD-1", ra=150, dec=20, distance=5, color='purple')
    bd2 = BrownDwarf("BD-1", ra=150, dec=25, distance=5, color='purple')
    get_angular_separation(bd1, bd1)


# if __name__ == "__main__":
#     # test_period_basis()
#     # test_semi_amp_basis()
#     # test_xyz_basis()
#     test_ang_sep()