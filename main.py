from my_point import MyPoint

point1 = MyPoint(3, 4, "A")
point2 = MyPoint(1, 2, "B")

point1.show_coord()
print(f"Відстань від місця відправлення для {point1.name}: {point1.calc_len()}")

point2.show_coord()
print(f"Відстань від місця відправлення для {point2.name}: {point2.calc_len()}")

point1.set_x(5)
point1.set_y(6)
point1.show_coord()
print(f"Відстань від місця відправлення для {point1.name}: {point1.calc_len()}")
