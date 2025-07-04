# JavaScript Functions Notes

## Function Definition
Functions in JavaScript are blocks of code designed to perform a specific task, defined using the `function` keyword, a name, optional parameters, and a body. They can be invoked multiple times and can return values.

### Example (Level 1 - Basic)
```javascript
function greet(name) {
  return "Hello, " + name + "!";
}
console.log(greet("Alice")); // Output: "Hello, Alice!"
```

### Example (Level 2 - Intermediate)
```javascript
function calculateArea(width, height) {
  if (width <= 0 || height <= 0) {
    return "Invalid dimensions";
  }
  return width * height;
}
console.log(calculateArea(5, 3)); // Output: 15
console.log(calculateArea(-1, 4)); // Output: "Invalid dimensions"
```

## Function Implementation
Functions can be implemented as function declarations, function expressions, or immediately invoked function expressions (IIFE). They encapsulate logic and can be reused.

### Example (Level 1 - Basic)
```javascript
// Function Declaration
function add(a, b) {
  return a + b;
}
console.log(add(2, 3)); // Output: 5

// Function Expression
const multiply = function(a, b) {
  return a * b;
};
console.log(multiply(2, 3)); // Output: 6
```

### Example (Level 2 - Intermediate)
```javascript
// Function Expression with Default Parameters
const createMessage = function(message, prefix = "INFO") {
  return `[${prefix}] ${message}`;
};
console.log(createMessage("Login successful")); // Output: "[INFO] Login successful"
console.log(createMessage("Error occurred", "ERROR")); // Output: "[ERROR] Error occurred"

// IIFE
(function() {
  console.log("This runs immediately!");
})();
```

## Arrow Function
Arrow functions (`=>`) provide a concise syntax for writing functions, with implicit return for single expressions and no `this` binding of their own.

### Example (Level 1 - Basic)
```javascript
const square = num => num * num;
console.log(square(4)); // Output: 16
```

### Example (Level 2 - Intermediate)
```javascript
const filterEvens = numbers => numbers.filter(num => num % 2 === 0);
console.log(filterEvens([1, 2, 3, 4, 5, 6])); // Output: [2, 4, 6]
```

### Example (Level 3 - Advanced)
```javascript
const processArray = (arr, callback) => arr.map(item => ({
  original: item,
  transformed: callback(item)
}));
console.log(processArray([1, 2, 3], num => num * 2));
// Output: [{ original: 1, transformed: 2 }, { original: 2, transformed: 4 }, { original: 3, transformed: 6 }]
```

## Exercise (For Better Understanding)
These exercises help reinforce the concepts of functions through practical application.

### Level 1 - Basic
Write a function that takes a number and returns whether it is positive, negative, or zero.

### Level 2 - Intermediate
Create a function that takes an array of numbers and returns a new array with each number doubled, using an arrow function.


### Level 3 - Advanced
Write a function that returns a counter object with methods to increment, decrement, reset, and get the current count, using a closure.