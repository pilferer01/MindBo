#Я хотел проверить на ввод 0 или -, но не знаю как лучше это сделать. В новом файле или в этом.
from pyfigure.figures import Triangle
import pytest


@pytest.mark.parametrize("a, b, c, result", [(3, 4, 5, True),
                                             (3, 6, 5, False),
                                             (3, 5, 6, False),
                                             (5, 12, 13, True),
                                             ])
def test_triangle_calculate_area(a, b, c, result):
    assert Triangle(a, b, c).check_right_triangle() == result
