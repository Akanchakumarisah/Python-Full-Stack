# Events Notes

## Events

Events are actions or occurrences that happen in the browser, such as a user clicking a button, typing in an input, or a webpage finishing loading. JavaScript can respond to these events to create interactive web applications. Events are part of the DOM and allow developers to execute code in response to user or system interactions.

### Importance of Events

- **Interactivity**: Enables dynamic responses to user actions (e.g., clicks, mouse movements, key presses).
- **User Experience**: Enhances web applications by making them responsive to user input.
- **Automation**: Handles system-generated events like page load or form submission.

---

## 1. Inline Event

Inline events are defined directly in the HTML markup using event attributes like `onclick`, `onchange`, or `onmouseover`. The JavaScript code is written as the attribute value.

### Explanation

- **Syntax**: `<element event="function()">`
- **Pros**: Simple and quick for small scripts.
- **Cons**: Mixes HTML and JavaScript, making code harder to maintain and less scalable.

**Example**:

```html
<button onclick="showMessage()">Click Me!</button>
<script>
    function showMessage() {
        alert("Inline event triggered!");
    }
</script>
```

---

## 2. External Event

External events are defined in a separate JavaScript file or `<script>` block, keeping HTML and JavaScript separate. They are attached to elements using DOM methods or properties like `onclick`.

### Explanation

- **Syntax**: `element.event = function() { ... }`
- **Pros**: Promotes clean code, better maintainability, and separation of concerns.
- **Cons**: Requires more setup than inline events.

**Example**:

```html
<button id="myButton">Click Me!</button>
<script>
    const button = document.getElementById("myButton");
    button.onclick = function() {
        alert("External event triggered!");
    };
</script>
```

---

## Event Object

The **Event object** is automatically passed to event handler functions and contains information about the event, such as the type of event, the target element, or mouse coordinates.

### Explanation

- **Access**: Available as a parameter in event handler functions.
- **Common Properties**:
  - `event.type`: Type of event (e.g., "click", "mouseover").
  - `event.target`: The element that triggered the event.
  - `event.preventDefault()`: Prevents default behavior (e.g., form submission).
  - `event.stopPropagation()`: Stops event bubbling to parent elements.

**Example**:

```html
<button id="myButton">Click Me!</button>
<script>
    const button = document.getElementById("myButton");
    button.onclick = function(event) {
        console.log(`Event Type: ${event.type}`);
        console.log(`Target Element: ${event.target.tagName}`);
    };
</script>
```

---

## Event Listeners

Event listeners are a more flexible way to handle events using the `addEventListener()` method. They allow multiple handlers for the same event and provide better control over event handling.

### Explanation

- **Syntax**: `element.addEventListener(event, handler, [options])`
- **Parameters**:
  - `event`: The event name (e.g., "click", "keydown").
  - `handler`: The function to execute when the event occurs.
  - `options` (optional): An object specifying characteristics like `once` (run once) or `capture` (use capture phase).
- **Advantages**: Supports multiple listeners for the same event, allows removal of listeners, and works with event delegation.

**Example**:

```html
<button id="myButton">Click Me!</button>
<script>
    const button = document.getElementById("myButton");
    
    function handleClick() {
        console.log("Button clicked with event listener!");
    }
    
    button.addEventListener("click", handleClick);
</script>
```

**Example with Options**:

```html
<button id="myButton">Click Me Once!</button>
<script>
    const button = document.getElementById("myButton");
    button.addEventListener("click",
```