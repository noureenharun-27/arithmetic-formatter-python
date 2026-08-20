# arithmetic-formatter-python
"Arithmetic Formatter — freeCodeCamp Scientific Computing with Python"

# Arithmetic Formatter

A Python function that takes a list of simple arithmetic problems (addition/subtraction) 
and formats them to look like they're arranged vertically, side-by-side — the way you'd 
write them out on paper.

Built as part of freeCodeCamp's [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) certification.

## What it does

Given a list like:

```python
["3801 - 2", "123 + 49"]
It returns:
  3801      123
-    2    +  49
------    -----
Validation rules

Max 5 problems at once
Only + and - operators allowed
Operands must be digits only, max 4 digits each
Optional second parameter shows the computed answer too

Concepts practiced

String formatting & alignment (rjust)
Input validation and custom error messages
Writing clean, testable functions
