import classTest

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
my_screen = Screen()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"],'l')
table.add_column("Type", ["Electric","Water","Fire",],'l')
print(table)