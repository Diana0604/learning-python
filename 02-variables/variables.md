# Hello world using a variable
## Step by Step
- Create a new python file using the commandline
- To do that, use the following command: `touch variables.py`. The file should appear on the workspace menu.
- Open the file `variables.py`
- Write the following line of code:
```python
hello = "hello world"
print(hello)
```
- From the terminal, use the following command: `python variables.py`
## What happened?
- The output from the terminal is the same output as before, even if the code has changed!
- We have **stored** the value `hello world` into a variable called `hello`. This variable could contain anything that we want.
- In fact, in the next step we will modify this variable so that it says something else.
## Quotation Marks!
- Again, we have used the quotation marks. But only when defining the variable!
- This is why they are important: if we do not use quotation marks, python thinks that we are trying to reference a variable that has appeared before. This is why we get the `not defined` error.
## What can go in a variable?
- Anything! Try replacing `hello world` by a number.
- Also: for numbers there is no need for quotation marks. Confusing? Yes. You will have to get used to it :/
## What is the use of variables?
- For example, greeting everyone. Let's do it.
- Define a few variables. For example, I will use your names
```python
name1 = "Paul"
name2 = "Qiu"
name3 = "Lucy"
name4 = "Zhaolin"
name5 = "Eva"
```
- Add this afterwards:
```python
print("Hello " + name1)
print("Hello " + name2)
print("Hello " + name3)
print("Hello " + name4)
print("Hello " + name5)
```
- Execute the program with `python variables.py`
## What happened?
- We defined a few variables.
- We used the operation `+` to combine them.
- We passed that combination to the method print.
## The real importance of quotation marks
- Alright so, let's try doing the same with numbers!
- Use the following code:
```python
number1 = "1"
number2 = "2"
```
- Add this afterwards:
```python
print(number1 + number2)
```
- Observe the result.
As you can see, we are obtaining `12`. What if we wanted to add them up? This is happening because we used quotation marks. The quotation marks are a way to indicate python that this is a sentence rather than a word. Sentences in programming are called `strings`. In order to let python know that we are working with numbers, not `strings`, we have to loose the quotation marks. Try this code instead:
```python
number1 = 1
number2 = 2

print(number1 + number2)
```