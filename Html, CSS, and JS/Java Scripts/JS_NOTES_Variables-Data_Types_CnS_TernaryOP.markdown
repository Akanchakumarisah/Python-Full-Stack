# JavaScript Notes

## Variables
Variables are used to store data values. In JavaScript, variables can be declared using `var`, `let`, or `const`.

### Example
```javascript
var name = "John"; // Older way, function-scoped
let age = 25; // Block-scoped, reassignable
const PI = 3.14; // Block-scoped, cannot be reassigned
```

## Declaration and Scoping
JavaScript variables can have global or local scope, depending on where they are declared.

- **Global Scope**: Variables declared outside any function or block are global and accessible everywhere.
- **Local Scope**: Variables declared inside a function or block are only accessible within that function or block.

### Example
```javascript
// Global Scope
let globalVar = "I'm global";

function exampleFunction() {
  // Local Scope
  let localVar = "I'm local";
  console.log(globalVar); // Accessible: "I'm global"
  console.log(localVar); // Accessible: "I'm local"
}

console.log(globalVar); // Accessible: "I'm global"
// console.log(localVar); // Error: localVar is not defined
```

## Data Types
JavaScript has several data types, including primitive and non-primitive types.

- **Primitive Types**: `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`
- **Non-Primitive Types**: `object` (includes arrays, functions, etc.)

### Example
```javascript
let str = "Hello"; // string
let num = 42; // number
let bool = true; // boolean
let nul = null; // null
let undef; // undefined
let sym = Symbol("id"); // symbol
let bigNum = 12345678901234567890n; // bigint
let obj = { name: "Alice", age: 30 }; // object
let arr = [1, 2, 3]; // array (object)
```

## Conditional Statements
Conditional statements control the flow of execution based on conditions.

### if, if-else, else-if
The `if` statement executes a block of code if a condition is true. `else-if` and `else` handle additional conditions or a fallback.

#### Example
```javascript
let age = 20;

if (age >= 18) {
  console.log("You are an adult.");
} else if (age >= 13) {
  console.log("You are a teenager.");
} else {
  console.log("You are a child.");
}
// Output: "You are an adult."
```

### switch-case
The `switch` statement evaluates an expression and executes code based on matching cases.

#### Example
```javascript
let day = "Monday";

switch (day) {
  case "Monday":
    console.log("Start of the week!");
    break;
  case "Friday":
    console.log("End of the workweek!");
    break;
  default:
    console.log("Just another day.");
}
// Output: "Start of the week!"
```

## Ternary Operator (?)
The ternary operator is a concise way to write an `if-else` statement in a single line. Syntax: `condition ? valueIfTrue : valueIfFalse`.

### Example
```javascript
let age = 16;
let status = age >= 18 ? "Adult" : "Minor";
console.log(status); // Output: "Minor"
```