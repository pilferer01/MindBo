#Я хотел проверить на ввод 0 или -, но не знаю как лучше это сделать. В новом файле или в этом.
from pyfigure.figures import Circle
import pytest


@pytest.mark.parametrize("i, result", [(5, 78.53981633974483),
                                       (3, 28.274333882308138),
                                       (1, 3.141592653589793),
                                       (4, 50.26548245743669),
                                       (300, 282743.3388230814),
                                       ])
def test_circle_calculate(i, result):
    assert Circle(i).calculate_area() == result
