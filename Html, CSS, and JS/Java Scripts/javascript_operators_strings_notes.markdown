# JavaScript Operators and String Literals Notes

## Operators

JavaScript operators perform operations on variables and values. They include arithmetic, assignment, comparison, logical, bitwise, ternary, and other specialized operators.

### Arithmetic Operators

Used for mathematical calculations.

#### Example

```javascript
let a = 10, b = 3;
console.log(a + b); // Addition: 13
console.log(a - b); // Subtraction: 7
console.log(a * b); // Multiplication: 30
console.log(a / b); // Division: 3.333...
console.log(a % b); // Modulus: 1
console.log(a ** b); // Exponentiation: 1000
console.log(++a); // Increment: 11
console.log(--b); // Decrement: 2
```

### Assignment Operators

Assign values to variables, often with shorthand for arithmetic operations.

#### Example

```javascript
let x = 5;
x += 3; // x = x + 3
console.log(x); // Output: 8
x *= 2; // x = x * 2
console.log(x); // Output: 16
x %= 5; // x = x % 5
console.log(x); // Output: 1
```

### Comparison Operators

Compare two values, returning a boolean.

#### Example

```javascript
let a = 5, b = "5";
console.log(a == b); // Equal (loose): true
console.log(a === b); // Strict equal: false
console.log(a != b); // Not equal (loose): false
console.log(a !== b); // Strict not equal: true
console.log(a > 3); // Greater than: true
console.log(a <= 5); // Less than or equal: true
```

### Logical Operators

Used for Boolean logic operations.

#### Example

```javascript
let x = true, y = false;
console.log(x && y); // AND: false
console.log(x || y); // OR: true
console.log(!x); // NOT: false
```

## String Literals

String literals are sequences of characters enclosed in quotes (single `'`, double `"`, or backticks `` ` `` for template literals). Template literals allow embedded expressions.

### Example

```javascript
let single = 'Hello';
let double = "World";
let template = `Greetings, ${single} ${double}!`;
console.log(single); // Output: "Hello"
console.log(double); // Output: "World"
console.log(template); // Output: "Greetings, Hello World!"
```