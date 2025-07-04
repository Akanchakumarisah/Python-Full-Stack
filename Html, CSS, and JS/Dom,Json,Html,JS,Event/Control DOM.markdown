# JavaScript DOM Notes

## What is DOM?
The **Document Object Model (DOM)** is a programming interface for web documents. It represents the structure of an HTML or XML document as a tree of objects, where each object (called a node) corresponds to a part of the document (e.g., elements, attributes, or text). JavaScript uses the DOM to interact with and manipulate the content, structure, and style of a webpage dynamically.

### Importance of DOM
- **Dynamic Web Pages**: Enables real-time updates to content, style, and structure without reloading the page.
- **Interactivity**: Allows user interactions (e.g., clicks, inputs) to trigger changes in the webpage.
- **Cross-Platform**: Works across browsers, providing a standardized way to access and modify web documents.
- **Foundation for Frameworks**: Libraries like React and Vue rely on DOM manipulation for rendering.

**Example**:
```javascript
// Accessing the DOM to change text content
document.getElementById("myId").textContent = "Hello, DOM!";
```

---

## DOM Nodes
DOM nodes are the individual components of the DOM tree. Each node represents a part of the document, such as an element, attribute, or text.

### Types of DOM Nodes
- **Element Node**: Represents HTML elements (e.g., `<div>`, `<p>`).
- **Text Node**: Contains the text inside elements.
- **Attribute Node**: Represents element attributes (e.g., `id`, `class`).
- **Document Node**: The root node of the document (e.g., `document`).

**Example**:
```html
<div id="example">Hello</div>
```
- `<div>`: Element node
- `id="example"`: Attribute node
- `Hello`: Text node

---

## DOM Manipulation and Its Methods
DOM manipulation involves modifying the structure, content, or style of a webpage using JavaScript. Below are common methods to select elements for manipulation.

### 1. Select by ID
The `getElementById()` method selects an element by its unique `id`.

**Example**:
```javascript
const element = document.getElementById("myId");
element.style.color = "blue";
```

### 2. Select by Class
The `getElementsByClassName()` method selects all elements with a specific class and returns an HTMLCollection.

**Example**:
```javascript
const elements = document.getElementsByClassName("myClass");
for (let element of elements) {
    element.style.backgroundColor = "yellow";
}
```

### 3. Select by Tag
The `getElementsByTagName()` method selects all elements with a specific tag name and returns an HTMLCollection.

**Example**:
```javascript
const paragraphs = document.getElementsByTagName("p");
for (let p of paragraphs) {
    p.textContent = "Updated paragraph!";
}
```

### 4. Query Selector
The `querySelector()` method selects the first element matching a CSS selector, and `querySelectorAll()` selects all matching elements, returning a NodeList.

**Example**:
```javascript
// Select first element with class 'myClass'
const element = document.querySelector(".myClass");
element.style.fontSize = "20px";

// Select all elements with class 'myClass'
const elements = document.querySelectorAll(".myClass");
elements.forEach(el => el.style.border = "1px solid black");
```

---

## Navigators
Navigator properties help traverse the DOM tree to access related nodes.

### 1. firstChild
The `firstChild` property returns the first child node of an element, including text nodes and comments.

**Example**:
```javascript
const parent = document.getElementById("parent");
const first = parent.firstChild; // Could be a text node
console.log(first);
```

### 2. firstElementChild
The `firstElementChild` property returns the first child element (ignoring text nodes or comments).

**Example**:
```javascript
const parent = document.getElementById("parent");
const firstElement = parent.firstElementChild; // First element node
firstElement.style.color = "red";
```

### 3. childNodes
The `childNodes` property returns a NodeList of all child nodes, including text nodes and comments.

**Example**:
```javascript
const parent = document.getElementById("parent");
const children = parent.childNodes;
children.forEach(node => console.log(node));
```

### 4. lastChild
The `lastChild` property returns the last child node of an element, including text nodes and comments.

**Example**:
```javascript
const parent = document.getElementById("parent");
const last = parent.lastChild; // Could be a text node
console.log(last);
```

### 5. nextSibling
The `nextSibling` property returns the next node in the DOM tree (including text nodes or comments).

**Example**:
```javascript
const element = document.getElementById("myId");
const next = element.nextSibling; // Next node
console.log(next);
```

---

## Targeting Attributes
Attributes are properties of DOM elements (e.g., `id`, `class`, `src`). JavaScript provides methods to get or set these attributes.

### 1. getAttribute(attr_name)
The `getAttribute()` method retrieves the value of a specified attribute.

**Example**:
```javascript
const element = document.getElementById("myImage");
const srcValue = element.getAttribute("src");
console.log(srcValue); // Outputs the image source
```

### 2. setAttribute(attr_name, value)
The `setAttribute()` method sets or updates the value of a specified attribute.

**Example**:
```javascript
const element = document.getElementById("myImage");
element.setAttribute("src", "new-image.jpg");
```

### 3. style()
The `style` property directly modifies an element's inline CSS styles.

**Example**:
```javascript
const element = document.getElementById("myId");
element.style.backgroundColor = "lightblue";
element.style.fontWeight = "bold";
```

---

## Insert Element
These methods allow you to create and insert new elements into the DOM.

### 1. createElement
The `createElement()` method creates a new element node with the specified tag name.

**Example**:
```javascript
const newDiv = document.createElement("div");
newDiv.textContent = "New Div!";
```

### 2. append
The `append()` method adds one or more nodes or strings as the last child of an element.

**Example**:
```javascript
const parent = document.getElementById("parent");
const newDiv = document.createElement("div");
newDiv.textContent = "Appended Div";
parent.append(newDiv);
```

### 3. prepend
The `prepend()` method adds one or more nodes or strings as the first child of an element.

**Example**:
```javascript
const parent = document.getElementById("parent");
const newDiv = document.createElement("div");
newDiv.textContent = "Prepended Div";
parent.prepend(newDiv);
```

### 4. before
The `before()` method inserts a node or string before the specified element.

**Example**:
```javascript
const element = document.getElementById("myId");
const newDiv = document.createElement("div");
newDiv.textContent = "Before Div";
element.before(newDiv);
```

### 5. after
The `after()` method inserts a node or string after the specified element.

**Example**:
```javascript
const element = document.getElementById("myId");
const newDiv = document.createElement("div");
newDiv.textContent = "After Div";
element.after(newDiv);
```