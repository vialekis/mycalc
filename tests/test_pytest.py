# import mycalc
# import pytest
#
# def test_div():
#     with pytest.raises(ZeroDivisionError):
#         mycalc.div(1,0)

import mycalc
import pytest


@pytest.mark.xfail(raises=ZeroDivisionError)

def test_div():
    mycalc.div(1, 0)