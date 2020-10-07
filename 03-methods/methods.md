# Methods
## What is a method?
A method is command that executes a specific segment of code. Some methods, such as `print`, are predefined by python. These methods are called [Built-In-Functions](https://docs.python.org/3/library/functions.html). In the hyperlink above you can see al these functions and how to use them! If we were using a different programming language, they would change. However, the basic Built-In-Functions (print, absolute value, round, change 'type of' variable...) will probably exist with a different name.

We can also define our own extra methods. In python, we can even redefine the Built-In-Functions! It is not recommended to do it, since they are here for a reason. However, if you do it you won't break it 'forever', only for that run of the program.
## Helloworld
Let's now define a method that says hello world:
```python
def hello_world():
    print("hello world")
```
### IMPORTANT things
- We always start a method definition with the command `def`. This let's python know that we are about to define a **new** method, rather than call an existing one. If we forget the `def`, it will think that we are calling a pre defined method and an error will occur.
- Method names CANNOT have spaces in between (try!)
- After the method name we need opening and closing brackets `()`. These brackets seem useless for now. But, remember print? In the print method, we need to let it know what we want to print. The brackets will help us do this.
- After the brackets, we will write `:` to let python know that we are starting the method definition.
- Everything that happens inside the method has to be indented, and everything that happens outside cannot be indented.
### Calling a method
Now, try executing the code above. Create a new file `methods.py`, insert the code, and execute it with `python methods.py`. What happens? Nothing!

The reason behind this is that we are **defining** the method, but not **calling** it afterwards. To call a method, after having defined it, all we have to do is:
```python
def hello_world():
    print("hello world")

hello_world()
```
## Variables in a method
We can also define variables to be passed to a method. For example, let's say we wanna say hi to several people (again).
```python
def greet(person):
    print("hello " + person)

greet("Eva")
greet("Zhaolin")
```
## But why are methods useful?
- They help us compactify. If I have to do the same thing over and over, and that thing is three lines of code, I can use a method which will occupy only one line!
- They prevent bugs and stupid mistakes. Imagine I decide that instead of saying **hello** to everyone, now I wanna say **hi**. If I had used print method for every person, i will need to change it as many times as people I had greeted. By using the method I only have to change it once.
- They help us understand what is going on. If I am rereading old code (or someone else's code), and I see `greet("Eva")`, I will immediatly know that that method is some sort of greeting that I am sending to Eva.
