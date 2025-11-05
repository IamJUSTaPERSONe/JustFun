import turtle
import keyboard


keyboard.add_hotkey('w', lambda: turtle.forward(10))
keyboard.add_hotkey('s', lambda: turtle.forward(10))
keyboard.add_hotkey('d', lambda: turtle.right(90))
keyboard.add_hotkey('a', lambda: turtle.left(90))
keyboard.add_hotkey('c', lambda: turtle.clearscreen())
keyboard.add_hotkey('e', lambda: turtle.up())
keyboard.add_hotkey('r', lambda: turtle.down())


turtle.bgcolor('orange')
turtle.exitonclick()
