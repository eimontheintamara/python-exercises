from sys import argv
import sys

print("How old are you?",end=' ')
age=input()

print("How tell are you?",end=' ')
height=input()

print("How much do you weight?",end=' ')
weight=input()

print(f"So, you're {age} old,{height} tall and {weight} heavy.")

script,filename=argv
txt=open(filename)
print("Here's you file{filename}:")
print(tx.read())

print("Type the filename again:")
file_again=input("> ")

txt_again=open(file_again)
print(txt_again.read())

print("let's practice everything.")
print("you \'d need to know \'about escapes with \\that do \n newlines and \t tabs.")

poem="""
\t The lovely world 
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from intuition 
and requires an explantion 
\n\twhere ther is none.
"""

print("**************")
print(poem)
print("**************")

five=10-2+3-6
print(f"This should be five:{five}")

def secret_formula(started)
  jelly_beans=started*500
  jars=jelly_beans/1000
  crates=jars/100
  return jelly_beans, jars, crates

start_point = 10000
beans, jars , crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
cats = 30
dogs = 15

if people < cats:
    print ("Too many cats! The world is doomed!")
if people < cats:
    print("Not many cats! The world is saved!")
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry!")
dogs += 5
if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")
