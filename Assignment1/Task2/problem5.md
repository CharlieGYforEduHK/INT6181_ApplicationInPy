# Problem 5

## Your prompt to generate solution

```plain
# your AI model here
    DeepSeek
# your prompt here
    Find any (real) solution to:  a x^2 + b x + c where coeffs = [a, b, c],return the solution as  a floating point number.
    Give me one answer, no need for multiple answer.Keep your response concise.
```

## Initial AI-generated solution

```python
# AI-generated solution here
import math

def sat(coeffs):
    a, b, c = coeffs
    if a == 0:
        return -c / b if b != 0 else 0.0
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    return (-b + math.sqrt(discriminant)) / (2*a)
```

## (optional) Your edited solution

Note: you may skip this section if AI-generated solution is correct.

The errors found in the AI-generated solution:
1. to be filled here
2. 
3.

Your edited solution:

```python
# your solution after debugging here
```

## Screenshots of interaction with AI

Please capture the screenshot and paste it here.
![alt text](image-14.png)