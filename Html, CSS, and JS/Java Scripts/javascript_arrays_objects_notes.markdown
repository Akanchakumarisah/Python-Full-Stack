# JavaScript Arrays and Objects Notes

## Arrays

Arrays are ordered, index-based collections of values in JavaScript, used to store multiple items under a single variable. They can hold any data type and support various methods for manipulation.

### Example

```javascript
// Creating and accessing an array
const fruits = ["apple", "banana", "orange"];
console.log(fruits[0]); // Output: "apple"
fruits.push("grape"); // Adds "grape" to the end
console.log(fruits); // Output: ["apple", "banana", "orange", "grape"]
```

### Example 

```javascript
// Using array methods
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(num => num * 2);
console.log(doubled); // Output: [2, 4, 6, 8, 10]
const evens = numbers.filter(num => num % 2 === 0);
console.log(evens); // Output: [2, 4]
```

### Example

```javascript
// Nested arrays and complex operations
const matrix = [[1, 2], [3, 4], [5, 6]];
const flattened = matrix.reduce((acc, curr) => acc.concat(curr), []);
const sum = flattened.reduce((acc, num) => acc + num, 0);
console.log(flattened); // Output: [1, 2, 3, 4, 5, 6]
console.log(sum); // Output: 21
```

## Objects

Objects are collections of key-value pairs, where keys are strings (or symbols) and values can be any data type. They are used to represent structured data.

### Example

```javascript
// Creating and accessing an object
const person = {
  name: "Alice",
  age: 25
};
console.log(person.name); // Output: "Alice"
person.job = "Developer"; // Adding a new property
console.log(person); // Output: { name: "Alice", age: 25, job: "Developer" }
```

### Example

```javascript
// Object methods and computed property names
const key = "id";
const user = {
  name: "Bob",
  [key]: 123,
  greet() {
    return `Hello, ${name}!`;
  }
};
console.log(user.id); // Output: 123
console.log(user.greet()); // Output: "Hello, Bob!"
```

### 

## Exercise

1. Create an array of colors and an object representing a car. Add a new color to the array and a new property to the car object.
2. Write a function that takes an array of numbers and returns an object with the sum and average of the numbers.