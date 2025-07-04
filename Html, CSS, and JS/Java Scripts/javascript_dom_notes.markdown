# JavaScript DOM Notes

## DOM (Document Object Model)

The Document Object Model (DOM) is a programming interface for web documents. It represents the structure of a webpage as a tree of objects, where each node is an element, attribute, or piece of text. The DOM allows JavaScript to interact with and manipulate the content, structure, and style of a webpage dynamically.

### Details
- **Structure**: The DOM represents a webpage as a hierarchical tree, with the `document` object as the root.
- **Nodes**: Elements, attributes, and text are nodes in the tree. For example, an HTML `<div>` is an element node, and its content is a text node.
- **Access**: JavaScript can access the DOM using methods like `document.getElementById()` or `document.querySelector()`.
- **Use Case**: Used for dynamically updating webpage content without reloading.

### Example
```javascript
// Accessing the DOM
const heading = document.getElementById("main-heading");
console.log(heading); // Outputs: <h1 id="main-heading">...</h1>
```

### DOM Diagram
Below is a simplified representation of a DOM tree for an HTML structure:

```
document
  └── html
      ├── head
      │   └── title
      │       └── "My Webpage"
      └── body
          ├── h1
          │   └── "Welcome"
          └── div
              ├── p
              │   └── "Hello, World!"
              └── button
                  └── "Click Me"
```

## DOM Manipulation

DOM manipulation involves changing the content, structure, or style of a webpage using JavaScript. Common tasks include updating element content, adding/removing elements, and modifying attributes or styles.

### Details
- **Content Modification**: Change text or HTML inside elements using properties like `innerText` or `innerHTML`.
- **Element Creation**: Create new elements with `document.createElement()` and add them to the DOM.
- **Attribute Manipulation**: Modify attributes like `class`, `id`, or `src` using methods like `setAttribute()`.
- **Style Changes**: Update CSS styles via the `style` property.
- **Removing Elements**: Remove elements with methods like `remove()` or `parentNode.removeChild()`.

### Example
```javascript
// HTML: <div id="container"><p>Old Text</p></div>

// Changing content
const paragraph = document.querySelector("#container p");
paragraph.innerText = "New Text";

// Creating and adding a new element
const newButton = document.createElement("button");
newButton.innerText = "Click Me";
document.getElementById("container").appendChild(newButton);

// Modifying style
paragraph.style.color = "blue";

// Removing an element
paragraph.remove();
```

## Event Listeners

Event listeners are used to detect and respond to user interactions or browser events (e.g., clicks, keypresses, mouse movements). They are attached to DOM elements using `addEventListener()`.

### Details
- **Syntax**: `element.addEventListener(event, callback, options)`.
- **Common Events**: `click`, `mouseover`, `keydown`, `submit`, `load`, etc.
- **Event Object**: The callback receives an event object with details like the target element or key pressed.
- **Removing Listeners**: Use `removeEventListener()` to stop listening for an event.
- **Event Bubbling/Capturing**: Events propagate through the DOM tree (default is bubbling, from child to parent).

### Example
```javascript
// HTML: <button id="myButton">Click Me</button>

// Adding a click event listener
const button = document.getElementById("myButton");
button.addEventListener("click", function(event) {
  console.log("Button clicked!", event.target);
  button.style.backgroundColor = "green";
});

// Adding a keydown event listener
document.addEventListener("keydown", function(event) {
  console.log(`Key pressed: ${event.key}`);
});
```

## DOM Diagram (Detailed)

Below is a more detailed DOM tree representation for an HTML document, showing how JavaScript can interact with it:

```
document
  └── html
      ├── head
      │   ├── meta (charset="UTF-8")
      │   └── title
      │       └── "My Webpage"
      └── body
          ├── h1 (id="main-heading")
          │   └── "Welcome to My Page"
          ├── div (id="container")
          │   ├── p (class="content")
          │   │   └── "This is a paragraph"
          │   └── button (id="myButton")
          │       └── "Click Me"
          └── script
              └── "JavaScript code for DOM manipulation"
```

### Explanation of Diagram
- **Root**: `document` is the entry point.
- **Elements**: `html`, `head`, `body`, etc., are element nodes.
- **Attributes**: `id`, `class`, and `charset` are attribute nodes.
- **Text**: Content like "Welcome to My Page" or "Click Me" are text nodes.
- **JavaScript Interaction**: Use methods like `document.getElementById("myButton")` to access the button or `document.querySelector(".content")` to target the paragraph.