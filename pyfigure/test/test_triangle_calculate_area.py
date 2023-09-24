#Я хотел проверить на ввод 0 или -, но не знаю как лучше это сделать. В новом файле или в этом.
from pyfigure.figures import Triangle
import pytest


@pytest.mark.parametrize("a, b, c, result", [(3, 4, 5, 6.0),
                                             (11, 12, 20, 56.718052681663885),
                                             (2, 3, 3, 2.8284271247461903),
                                             (300, 200, 400, 29047.37509655563),])
def test_triangle_calculate_area(a, b, c, result):
    assert Triangle(a, b, c).calculate_area() == result

