# импорты библиотек
import main
from graphlern import Pixel, Message


# объявление переменных(констант)
GRID_WIDTH = 10
GRID_HEIGHT = 10
PIXEL_SIZE = 50
BACKGROUND_COLOR = "#ffeba1"
SOUND = ""


 

# координаты x пикселей апельсина

x_coords_when_y_equals_1 = []
 

# отрисовка
def draw(window):
    # Здесь пиши свой код
    
    Pixel(window, x=1, y=2, color="orange", size=PIXEL_SIZE)
