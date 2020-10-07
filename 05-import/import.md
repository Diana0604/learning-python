# Importing
When we talk about importing in computer science, we are talking about using code that has been written somewhere else, either by us or by another person. This is useful for two main reasons:
- If I am writing a very long program, I do not want to have one single file with thousands of lines. Rather, I will use different files. Each file will be in charge of a specific part of the program. For example, in our fax machine, I have different files the following files:
    - `calls` to launch calls
    - `lights` to control the lights
    - `music` to control the music
    - `utils` is a generic folder where I store non-related but necessary methods
    - Finally, I have one file called `manager` which executes the different files according to necessity. In this file I **import** the other files, so that I can use them as if they had been defined in the same file
- If I want to do something that someone else has already done, I can use their code rather than coding everything again! There's two ways that I might want to import someone else's code.
  - Built in packages. In built in packages, I can import stuff that is pre-built in python. The reason why I can't access all the code at once is just for performance. If everything was compiled every time I run a program, it would take a very long time. This is why everything is compactified into smaller files, that we can import.
  - Packages that other people has done. Sometimes, I want to do something but I am not the first one to try it. Someone else might have programmed it before me! We can download their code and import it into our code.

## Import my own code
- Let's create a file called `tools.py`
- Let's create another file called `workshop.py`
- We will define tools in the tools file that can be used in the workshop
- Let's begin by creating a hammer:
```python

```