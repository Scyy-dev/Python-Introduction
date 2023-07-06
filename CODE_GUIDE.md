# Welcome to Python!

This guide serves as an introduction to the Python programming language, covering the key basics to making a simple
choose your own adventure game!

<br><br>

# What is Python?

Python is a programming language aimed to be easy to learn, easy to read, easy to get started with, and enjoyable to
program with. It is arguably one of the best programming languages to start out with because of those features, and it's
incredibly powerful at what it can do.

<br><br>

# How do I get started?

To dive straight into Python, you can download the Python application at
the [official Python website](https://www.python.org/downloads/).

There are also other alternatives available that let you edit code online, such as
the [W3Schools online editor](https://www.w3schools.com/python/trypython.asp?filename=demo_default)
or [replit](https://replit.com/)

It's important that you learn how to run your code - online editors have an obvious 'run' button, but the offline editor
from Python requires making a file, saving it locally, and then running it.

Because your choice of environment can vary greatly on preference, I highly recommend using online resources like Google
search, Youtube and the Python website to learn about how to use the environment.

Within this environment will be something called a *console*. The console is responsible for all the text output of the
program. We use the console to see our programs output. We'll be seeing plenty of it the more code we write.

<br><br>

# Our First Program!

Our first program will be the classic known within the programming community - a 'hello world' program. This program
involves writing code that shows the text 'hello world' on screen in the simplest way possible for the language.

For python, this means we need to learn about 3 key things - syntax, strings, and functions.

<br>

### Syntax

Syntax is what drives the way you write code. In the same way that it doesn't make sense to say english words in a
random order, you can't just put together random characters, symbols and words in programming together and expect it to
work! It requires learning about how the language works to correctly use the syntax - just like any spoken language!

<br>

### Strings

Strings are the code version of text. Any time you see symbols, characters, sentences and more, those can all be
considered "strings". We use strings any time we want to work with text related content in a program.

When writing strings in code, you use apostrophes. For example:

```python
'I am a string!'
```

Because the text was wrapped inside of the apostrophes, it can be considered a 'string'.

<br>

### Functions

When you write code, you need to work with what the computer can offer. The way that happens is through functions -
functions are a collection of pre-written code to save you time and effort, and to do a particular task.

If you're familiar with functions from math, they work the same way. They're broken down into 4 components:

1. The name of the function
2. The inputs of the function
3. The action of the function
4. The output of the function

The first function we'll get to see is the `print` function. The `print` function is a special function in Python that
takes any input, and prints it out on our screen! How neat is that? An important thing to note is that it doesn't
actually *print* anything - it just does stuff on our screen, we won't be seeing any paper here!

<br>

### Our first bit of code!

In the editor you've chosen, write the following line of code:

```python
print("Hello, world!")
```

If you're using the offline editor, you'll need to save the file first. Once it's all saved, you can run it using the
menu or the run button for an online editor. If it all worked, the text `Hello, world!` should of appeared on the
console!

If you saw the text, congratulations! You've written your first bit of code and run it. You've made the first step to
learning to be a Python programmer.

<br><br>

# Storing Data

When working with code, an important part of the code is to store data. Data comes in many different shapes and sizes,
so we'll learn about how we can store data and the different *data types* there are.

<br>

### Variables!

To store data in code, the most basic form is to use a *variable*. A variable is simple - it's a named box of data.

Imagine a room full of named boxes. Each box has a label on it, and stores different things. One box might contain 50
apples, another box might contain a school textbook, another box might be the weekly shopping list. That's exactly how a
variable works.

Variables follow a particular syntax in Python. To use a variable, you need a *name*, an *equals sign* (`=`), and a
*value*.

Let's try and use our first variable. We're going to put the `Hello, world!` string we used earlier inside a variable!

**Tip!**
any time you see a big block of code, that means you can write (or copy-paste!) that code in your editor.

```python
my_var = "Hello, world!"
```

We've now used a variable!

Now we should put it to use. Remember the `print` function? Lets try combining the two!

```python
my_var = "Hello, world!"
print(my_var)
```

We've now put a variable to use! Go us!

<br>

### Data Types!

Now we know how to *store* data, we need to figure out *what* it is we're actually storing.