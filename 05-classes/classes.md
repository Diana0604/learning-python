# Classes
## The basics
 For now we have worked with two elements: Integers (1,2,3,4...) and Strings ("hello world", "Zhaolin", "Diana", "12"...). These are two examples of what is known as types. There are more types (check [Built-In-Types](https://developers.google.com/edu/python/strings)).

We can also define our own types. That is, however, very complicated and not very useful in general. The idea is that types are as simple as possible. And all the simplest types have already been given to us by python!

When we want to work with something that is more complex than a type we will use what is called as an object or class. Let's see an example. We will work with Qrumpet show, just because it's fun! 

In `classes.py`, define the class Qrumpet:
```python
class Qrumpet:
    shape = "qrumpet-like shape"
    taste = "amazing"
    number_of_holes = 15
```
To create a new Qrumpet, we can now use the method:
```python
qrumpet = Qrumpet()
```
**IMPORTANT:** The new element cannot be called Qrumpet. i.e., it cannot have the same name as the class name. Changing a capital to lower case is enough.

**NOTE:** Traditionally, classes names begin with capital letter.

To access an object's property, we can use the syntax: `object.property`. For example, we can check `qrumpet.shape`, which will give us the shape of the qrumpet. Try adding this to your code this:

```python
print("The qrumpet's shape is: " + qrumpet.shape)
```

Let's replace the definition of `qrumpet` by these two lines:
```python
qrumpet1 = Qrumpet()
qrumpet2 = Qrumpet()
```

Now, we'll modify the shape of qrumpet1:
```python
qrumpet1.shape = "bitten"
```

Try printing the two shapes:
```python
print("qrumpet1's shape is: " + qrumpet1.shape)
print("qrumpet2's shape is: " + qrumpet2.shape)
```

Run this code and see what happens! So, after creating an object, we can modify the predefined properties to keep tracked on what's gone through them. For example, if I'm keeping track on 2 qrumpets, and Zhaolin bites one of them, I will have to modify that qrumpet's shape.

## Define properties upon creation
As we have now defined the class Qrumpet now, the default state of a Qrumpet is `qrumpet-like shape`, the taste is `amazing`, and the number of holes is `15`. If at the beginning of the program I have, for example, 5 perfect amazing qrumpets, from which 2 have been bitten, and 3 extra moldy qrumpets which tastes really bad, I have to modify all these properties after creating all the qrumpets! There is a way to let python know that some properties can be modifiet upon creation of a new instance. To do this we use the method `__init__(self)`. Rewrite the definition of Qrumpet into:
```python
class Qrumpet:
    def __init__(self):
        self.shape = "qrumpet-like shape"
        self.taste = "amazing"
        self.number_of_holes = 15
```
If you try the code now, it will do exactly the same as before. Let's now try this:
```python
class Qrumpet:
    def __init__(self, shape, taste, number_of_holes):
        self.shape = shape
        self.taste = taste
        self.number_of_holes = number_of_holes
```

If you run the code, you will get the following error:
```
Traceback (most recent call last):
  File "classes.py", line 6, in <module>
    qrumpet1 = Qrumpet()
TypeError: __init__() takes exactly 3 arguments (1 given)
```

To recover what we had before, you'll have to modify the lines where you define qrumpets for this:
```python
qrumpet1 = Qrumpet("qrumpet-like shape", "amazing", 15)
qrumpet2 = Qrumpet("qrumpet-like shape", "amazing", 15)
```
Now, let's try some properties. If you do:
```python
qrumpet1 = Qrumpet("triangle", "amazing", 402)
qrumpet2 = Qrumpet("qrumpet-like shape", "bad and moldy", 15)
```
You have two completely different qrumpets.

## Mix default and definable properties
Let's imagine the situation where I have 20 qrummpets with amazing taste, and 1 qrumpet which is moldy. With this new method, I will still ahve to create my 20 good qrumpets one by one, specifying how good they are! There is away to mix a default property, with the possibility of redefining it. Try it:
```python
class Qrumpet:
    def __init__(self, shape, number_of_holes, taste = "amazing"):
        self.shape = shape
        self.taste = taste
        self.number_of_holes = number_of_holes
```

Note that the default has to go at the end. Now, this means that the attribute `taste` is optional. I can either create a Qrumpet by writing:

```python
qrumpet1 = Qrumpet("triangle", 402)
qrumpet2 = Qrumpet("qrumpet-like shape", 15, taste="bad and moldy")
```

Note that I have written `taste="bad and moldy"` for the optional attribute. That would not be necessary. However, when we have many optional attributes, if I only want to set a few, that's the easiest way to do it!