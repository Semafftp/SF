from rectangle1 import Rectangle, Square ,Circle
rect_1=Rectangle(3,4)
rect_2=Rectangle(12,5)
print(rect_1.get_area())
print(rect_2.get_area())

square_1= Square(5)
square_2= Square(10)
print(square_1.get_area_square(),
      square_2.get_area_square())
figures = [rect_1,rect_2,rect_1,rect_2]
for figure in figures:
      if isinstance(figure,Square):
            print(figure_get_area_square())
      else:
            print(figure.get_area())
circle_1=Circle(8)
circle_2=Circle(21)
print(circle_1.get_area_Circle(),
      circle_2.get_area_Circle())

