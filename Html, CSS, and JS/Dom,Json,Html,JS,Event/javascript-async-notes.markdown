# JavaScript Asynchronous Programming Notes

## Async-Await

**Async-Await** is a syntactic feature in JavaScript that simplifies working with asynchronous operations by making them appear synchronous. Built on top of Promises, it enhances code readability and maintainability.

### Explanation
- **Async Function**: Declared with the `async` keyword, it always returns a Promise, even if the return value is not explicitly a Promise.
- **Await Keyword**: Used inside `async` functions to pause execution until a Promise resolves or rejects, returning the resolved value or throwing an error.
- **Purpose**: Simplifies handling of asynchronous tasks like API calls, file operations, or timers.
- **Pros**: Cleaner syntax than Promise chains, easier to read and debug.
- **Cons**: Must be used within an `async` function; not ideal for parallel Promise execution without additional handling.

---

## Example of Async-Await

Here’s a practical example demonstrating Async-Await with a simulated delay and an API call.

**Example**:
```javascript
async function getUserData() {
    try {
        // Simulate a delay
        await new Promise(resolve => setTimeout(resolve, 1000));
        console.log("Waited for 1 second");

        // Fetch data from an API
        const response = await fetch('https://jsonplaceholder.typicode.com/users/1');
        const user = await response.json();
        console.log("User:", user.name);
    } catch (error) {
        console.error("Error:", error.message);
    }
}
getUserData(); // Logs "Waited for 1 second" then "User: Leanne Graham" (or error)
```

---

## Promises & Modules

### Promises
A **Promise** is an object representing the eventual completion or failure of an asynchronous operation. It provides a way to handle asynchronous results with `.then()` and `.catch()`.

**States**:
- **Pending**: Initial state, neither fulfilled nor rejected.
- **Fulfilled**: Operation completed successfully, returns a value.
- **Rejected**: Operation failed, returns an error.

**Syntax**:
```javascript
const promise = new Promise((resolve, reject) => {
    // Async task
    if (/* condition */) resolve(value);
    else reject(error);
});
```

**Example**:
```javascript
const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("Success after 2 seconds!"), 2000);
});
myPromise.then(result => console.log(result)); // Logs "Success after 2 seconds!"
```

### Modules
**Modules** allow modularizing JavaScript code into separate files, promoting reusability and organization. They use `import` and `export` statements, often paired with asynchronous operations like Promises.

**Syntax**:
- Export: `export { item }` or `export default item`
- Import: `import { item } from './file.js'`

**Example** (`utils.js`):
```javascript
export function delayedMessage() {
    return new Promise((resolve) => {
        setTimeout(() => resolve("Message from module"), 1000);
    });
}
```

**Example** (`main.js`):
```javascript
import { delayedMessage } from './utils.js';
delayedMessage().then(msg => console.log(msg)); // Logs "Message from module"
```

**HTML Setup**:
```html
<script type="module" src="main.js"></script>
```

---

## How Promises Are Related to Async-Await

**Async-Await** is a higher-level abstraction built on **Promises**. It provides a more intuitive way to handle asynchronous operations by avoiding explicit `.then()` and `.catch()` chains.

### Explanation
- **Async Function**: Wraps its return value in a Promise, even for synchronous values.
- **Await**: Acts like `.then()`, pausing execution until the Promise resolves, and directly returns the resolved value.
- **Error Handling**: `try-catch` with Async-Await replaces `.catch()` for handling rejections.
- **Relation**: Async-Await is syntactic sugar for Promises, offering a cleaner, more synchronous-looking syntax.

**Example** (Comparing Promises and Async-Await):
```javascript
// Promise-based
function getData() {
    return new Promise((resolve) => {
        setTimeout(() => resolve("Data retrieved"), 1000);
    });
}
getData().then(data => console.log(data));

// Async-Await
async function fetchAsync() {
    const data = await getData();
    console.log(data);
}
fetchAsync(); // Logs "Data retrieved"
```

---

## Error Handling

Error handling is essential for robust asynchronous code. Both Promises and Async-Await provide mechanisms to catch and handle errors gracefully.

### Promises Error Handling
- Use `.catch()` to handle rejections.
- Use `.finally()` for cleanup tasks that run regardless of success or failure.

**Example**:
```javascript
const promise = new Promise((resolve, reject) => {
    setTimeout(() => reject("Failed to load"), 1000);
});
promise
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error))
    .finally(() => console.log("Operation complete"));
```

### Async-Await Error Handling
- Use `try-catch` blocks to catch errors in `async` functions.
- Optionally use `finally` for cleanup.

**Example**:
```javascript
async function fetchWithError() {
    try {
        const response = await fetch('https://invalid-url');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error:", error.message);
    } finally {
        console.log("Fetch attempt complete");
    }
}
fetchWithError(); // Logs error and "Fetch attempt complete"
```

---

## Fetch API for HTTP Request

The **Fetch API** is a modern interface for making HTTP requests (e.g., GET, POST) and returns a Promise, making it ideal for use with Async-Await.

### Explanation
- **Syntax**: `fetch(url, [options])`
- **Returns**: A Promise resolving to a `Response` object.
- **Key Methods**:
  - `response.json()`: Parses JSON from the response.
  - `response.text()`: Returns response as text.
  - `response.status`: HTTP status code (e.g., 200 for success, 404 for not found).
- **Options**: Customize requests with `method`, `headers`, `body`, etc.
- **Error Handling**: Fetch only rejects on network errors; check `response.ok` for HTTP errors.

**Example** (GET Request):
```javascript
async function fetchUser() {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/users/1');
        if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
        const user = await response.json();
        console.log("User:", user.name);
    } catch (error) {
        console.error("Fetch error:", error.message);
    }
}
fetchUser(); // Logs "User: Leanne Graham" or error
```

**Example** (POST Request):
```javascript
async function createPost() {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: 'New Post',
                body: 'This is a test post.',
                userId: 1,
            }),
        });
        if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
        const post = await response.json();
        console.log("Created Post:", post);
    } catch (error) {
        console.error("Post error:", error.message);
    }
}
createPost(); // Logs created post or error
```