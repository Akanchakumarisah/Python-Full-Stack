# CSS Grid, Flexbox, and Animations Notes

## CSS Grid

**CSS Grid** is a two-dimensional layout system for arranging elements in rows and columns, offering precise control over complex layouts.

### Key Concepts
- **Grid Container**: The parent element with `display: grid`.
- **Grid Items**: Direct children of the container.
- **Grid Lines**: Dividers between rows and columns.
- **Grid Tracks**: Rows or columns.
- **Grid Areas**: Named regions for placing content.

### Basic Syntax
```css
.container {
    display: grid;
    grid-template-columns: 100px 100px 100px; /* 3 columns */
    grid-template-rows: 50px 50px; /* 2 rows */
    gap: 10px; /* Space between grid items */
}
```

### Example
A simple 2x3 grid:
```html
<div class="container">
    <div class="item">1</div>
    <div class="item">2</div>
    <div class="item">3</div>
    <div class="item">4</div>
</div>
```
```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr; /* Equal-width columns */
    grid-template-rows: auto auto; /* Auto-sized rows */
    gap: 10px;
}
.item {
    background-color: lightblue;
    padding: 10px;
}
```

### Key Properties
- `grid-template-columns`/`grid-template-rows`: Define column/row sizes (e.g., `100px`, `1fr` for fraction).
- `gap`: Sets spacing between grid items.
- `grid-column`/`grid-row`: Positions items (e.g., `grid-column: 1 / 3` spans two columns).
- `grid-template-areas`: Names areas for layout.
  ```css
  .container {
      grid-template-areas:
          "header header"
          "main sidebar";
  }
  .header {
      grid-area: header;
  }
  ```

### Best Practices
- Use `fr` units for flexible layouts.
- Combine with media queries for responsive designs.
- Use `grid-template-areas` for semantic layouts.

---

## Flexbox

**Flexbox** (Flexible Box Layout) is a one-dimensional layout system for arranging items in a row or column, ideal for responsive designs.

### Key Concepts
- **Flex Container**: Parent with `display: flex`.
- **Flex Items**: Direct children of the container.
- **Main Axis**: Primary direction (row or column).
- **Cross Axis**: Perpendicular to the main axis.

### Basic Syntax
```css
.container {
    display: flex;
    flex-direction: row; /* or column */
    justify-content: space-between; /* Align along main axis */
    align-items: center; /* Align along cross axis */
}
```

### Example
A row of centered items:
```html
<div class="container">
    <div class="item">Item 1</div>
    <div class="item">Item 2</div>
    <div class="item">Item 3</div>
</div>
```
```css
.container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 10px;
}
.item {
    background-color: lightgreen;
    padding: 10px;
}
```

### Key Properties
- `flex-direction`: Sets main axis (`row`, `column`, `row-reverse`).
- `justify-content`: Aligns items on main axis (e.g., `flex-start`, `space-around`).
- `align-items`: Aligns items on cross axis (e.g., `center`, `stretch`).
- `flex-wrap`: Allows items to wrap (`wrap`, `nowrap`).
- `flex`: Controls item size (e.g., `flex: 1` for equal sizing).

### Best Practices
- Use for one-dimensional layouts (e.g., navigation bars).
- Combine with `gap` for spacing.
- Test responsiveness with `flex-wrap`.

---

## CSS Animations

**CSS Animations** allow elements to transition smoothly between styles, creating dynamic effects like fades, slides, or rotations.

### Key Concepts
- **Keyframes**: Define animation stages.
- **Animation Properties**: Control timing, duration, and behavior.

### Basic Syntax
```css
@keyframes slideIn {
    from {
        transform: translateX(-100%);
    }
    to {
        transform: translateX(0);
    }
}
.element {
    animation: slideIn 1s ease-in-out;
}
```

### Example
A fading box:
```html
<div class="box"></div>
```
```css
.box {
    width: 100px;
    height: 100px;
    background-color: coral;
    animation: fade 2s infinite;
}
@keyframes fade {
    0% {
        opacity: 1;
    }
    50% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
}
```

### Key Properties
- `animation-name`: Links to `@keyframes`.
- `animation-duration`: Time for one cycle (e.g., `2s`).
- `animation-timing-function`: Speed curve (e.g., `ease`, `linear`).
- `animation-iteration-count`: Number of cycles (e.g., `infinite`, `3`).
- `animation-delay`: Delay before starting (e.g., `1s`).

### Transitions (Simpler Alternative)
For simple state changes:
```css
.button {
    background-color: blue;
    transition: background-color 0.3s ease;
}
.button:hover {
    background-color: green;
}
```

### Best Practices
- Use animations sparingly to avoid overwhelming users.
- Test performance on different devices.
- Combine with `:hover` or JavaScript for interactivity.

---

## Practice Exercises

1. Create a 3x2 CSS Grid layout with a header spanning all columns.
2. Build a responsive navigation bar using Flexbox.
3. Animate a box to slide in from the left when the page loads.
4. Combine Grid and Flexbox to create a webpage layout with a header, sidebar, and main content.

---