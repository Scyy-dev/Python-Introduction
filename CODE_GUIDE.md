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

# Working with Data

When working with code, an important part of the code is to store and manipulate data. Data comes in many different
shapes and sizes,
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

There are quite a number of data types in Python, and the topic can get complicated fast. So we're going to keep it
simple and straightforward.

Number - the numbers you're familiar with from math.
String - text, symbols and characters. We've seen this already with our `Hello, world!`
Boolean - a true/false value. Very useful for logic - we'll see lots of this later!

Lets try using all of them, all at once!

```python
my_num = 5
my_string = "World, hello!"
my_boolean = True
```

Whew! There's more complicated data types to cover, but for now we can get pretty far with these.

<br>

### Operations!

We have a way to *store* data, and we know *what* the data is, but what do we actually *do* with the data?

Introducing operations! They create ways for the data to interact with each other.

Most of these come from Math - they should all look or sound very familiar!

* Addition - adds 2 variables together. `var_1 + var_2`
* Subtraction - subtracts right variable from the left variable. `var_1 - var_2`
* Multiplication - multiplies 2 variables together. `var_1 * var_2`
* Division - divides right variable from the left variable. `var_1 / var_2`

Operations don't have to apply

```python
result = 10 * 5
next_result = result / 5
final_result = next_result + 2
```

<br>

### Comments!

Sometimes, you want to write helpful messages in your code without writing actual code. This is a very common thing, and
it's called code commenting! Code comments are a great way to explain what's going on in the code if it's hard to read
or understand.

Comments in Python are done using the `#` symbol. Anything written after the `#` symbol is *completely ignored* when the
program runs.

```python
print("Hello, world!")  # This is a comment! It will never be treated as code!

my_var = '5'  # Fun fact! Numbers can be strings too if they're in between quotation marks / apostrophes!
```

<br><br>

# Our Second Program!

We're going to tackle a harder project now. Using everything we've learned so far, plus 2 new functions, we're going to
make a *simple calculator*.

<br>

### How it works

Our calculator program will work like so:

1. The program asks the user to enter a number
2. The program asks the user to enter another number
3. The program calculates the sum of the 2 numbers
4. The program prints the result of the calculation

There's a lot to unpack there! We'll take it step-by-step so we can get this program done.

<br>

### Step 1: Asking for a number

The first step requires us to understand how Python gets user input. This involves using a brand new function:
the `input` function!

The `input` function prints a message to the console (just like the `print` function!) but then also waits for the user
to type something into the console. When the user hits enter, the *string* that the user typed into the console is then
*returned* from the function.

That sounds really confusing compared to what we've done so far, so lets see it in action:

```python
user_input = input("Please type something:")  # Try typing something when your program runs
print(user_input)  # What you just typed will be printed!
```

So for example, say I type `hello` in the console when the program runs, and then hit enter. `hello` will be printed
back at me!

<br>

Now let's try asking for a number.

```python
num1 = input("Please enter a number:")
```

Great! We've got our program to *ask the user to enter a number*. Step 1 done!

<br>

### Step 2: Asking for another number

We've done this already! This should be as easy as copy-paste, and tweaking it slightly. An important thing to know is
that if we don't change the variable name, we'll overwrite what was in the variable!

Think of it as putting something in the box when there is something there already magically deletes what was there
already.

You can see this in action:

```python
my_var = 5
my_var = 6
print(my_var)  # we get 6. The 5 went *poof*
```

So now when we copy-paste that code, let's make sure we get it right:

```python
num1 = input("Please enter a number:")
num2 = input("Please enter a number:")
```

Good stuff! Step 2 done: *ask the user to enter another number*.

<br>

### Step 3: Calculate the sum

We now need to calculate the sum of the 2 numbers. To get the sum of the 2 numbers, we have to *add* them together.

Using our previous knowledge of operators, we use the `+` symbol for add, and we want to add the 2 variables we used
earlier (`num1` and `num2`)

Our code should now look like this:

```python
num1 = input("Please enter a number:")
num2 = input("Please enter a number:")
result = num1 + num2
```

<br>

### Step 4: Print the Output

We've done the input, we've done the calculation, now we need the output!

We use the `print` function we're familiar with now to do that. Let's print the result!

```python
num1 = input("Please enter a number:")
num2 = input("Please enter a number:")
result = num1 + num2
print(result)
```

Now let's try running it! I'm going to try a simple 1 + 1.

Uh oh. That's not good.

<br>

### Operators on Strings

We encountered an interesting issue - when we tried `1` + `1`, we got `11`! That's not right at all! Even in binary it's
not right!

The issue comes from the *data types* we're working with.

The `input` function gives us Strings. but we don't want strings! We want numbers!

To fix this, we need to convert the strings to numbers. To do this, we use a new function, called `float`.

This function converts the value given to a float, which is a specific type of number that supports decimal points (
e.g. `3.14`)


