
```md

## Syntax and Examples of Match Case in Python
Now that you understand the benefits of Match Case statements, let’s delve into their syntax and see them in action with practical examples.

## Basic Syntax:
The basic syntax of a Match Case statement follows this structure:

match expression:
    case pattern1:
        code_block_1
    case pattern2:
        code_block_2
    ...
    case pattern_n:
        code_block_n
    # Optional: _ (wildcard) for default case
expression: This is the value you want to match against different patterns.

case pattern: Each case statement defines a pattern to match against the expression.
code_block: The code block associated with a matching pattern is indented and executed.


_ (wildcard): An optional _(underscore) can be used as a wildcard pattern to match anything not explicitly covered by other cases. This serves as a default case.

### Matching Specific Values:
Let’s see how Match Case simplifies checking for specific values:

day = input("Enter a day of the week (Monday-Sunday): ").lower()

match day:
    case "monday":
        print("Ugh, Mondays...")
    case "tuesday":
        print("Just another workday...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there...")
    case "friday":
        print("TGIF!")
    case "saturday" | "sunday":  # Match multiple values with pipe (|)
        print("Weekend vibes!")
    case _:
        print("Invalid day entered.")
##
In this example, the day variable is matched against specific weekdays. Each matching case executes its corresponding code block, printing a message based on the user’s input. Notice how the | (pipe) operator allows matching against multiple values in a single case.
```

## Mataching data types 
```md
Matching Data Types:
Match Case can also be used to match against data types:

value = input("Enter a value (number or string): ")

match value:
    case int():
        print("You entered an integer:", value)
    case str():
        print("You entered a string:", value)
    case _:
        print("Invalid data type entered.")

```
