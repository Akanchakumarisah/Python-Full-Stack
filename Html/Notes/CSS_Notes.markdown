# CSS Notes

**CSS** (Cascading Style Sheets) is a styling language used to control the appearance and layout of HTML elements on a webpage. It enhances the visual presentation of web content, making it more engaging and user-friendly.

---

## What is CSS?

CSS defines the **style** of HTML elements, such as colors, fonts, sizes, and positioning. It separates presentation from content, allowing developers to maintain and update styles independently of the HTML structure.

**Key Purposes**:
- Style HTML elements (e.g., colors, fonts).
- Control layout (e.g., positioning, spacing).
- Ensure consistent design across webpages.

---

## CSS Syntax

CSS rules consist of a **selector** and a **declaration block**:

```css
selector {
    property: value;
    property: value;
}
```

- **Selector**: Targets HTML elements (e.g., `h1`, `.class`, `#id`).
- **Declaration Block**: Contains properties and their values inside `{}`.
- **Property**: What to style (e.g., `color`, `font-size`).
- **Value**: How to style it (e.g., `blue`, `16px`).

**Example**:
```css
p {
    color: blue;
    font-size: 16px;
}
```

---

## Adding CSS to HTML

There are three ways to apply CSS:

1. **External CSS** (Recommended):
   - Use a separate `.css` file linked via `<link>` in the HTML `<head>`.
   ```html
   <link rel="stylesheet" href="styles.css">
   ```

2. **Internal CSS**:
   - Place CSS inside a `<style>` tag in the HTML `<head>`.
   ```html
   <style>
       h1 {
           color: green;
       }
   </style>
   ```

3. **Inline CSS**:
   - Add CSS directly to an element’s `style` attribute (avoid for maintainability).
   ```html
   <p style="color: red;">Text</p>
   ```

---

## CSS Selectors

Selectors target HTML elements for styling.

### 1. Element Selector
Targets all instances of an HTML tag.
```css
p {
    color: black;
}
```

### 2. Class Selector
Targets elements with a specific `class` attribute (use `.class-name`).
```css
.my-class {
    background-color: yellow;
}
```
```html
<p class="my-class">Styled paragraph</p>
```

### 3. ID Selector
Targets a single element with a unique `id` (use `#id-name`).
```css
#unique {
    font-weight: bold;
}
```
```html
<div id="unique">Unique div</div>
```

### 4. Universal Selector
Targets all elements (use `*`).
```css
* {
    margin: 0;
}
```

### 5. Grouping Selectors
Apply the same styles to multiple selectors.
```css
h1, h2, .title {
    color: navy;
}
```

### 6. Descendant Selector
Targets elements inside another element.
```css
div p {
    font-size: 14px;
}
```

---

## Common CSS Properties

### 1. Text and Font Properties
- `color`: Text color (e.g., `red`, `#FF0000`).
- `font-size`: Text size (e.g., `16px`, `1em`).
- `font-family`: Font type (e.g., `Arial, sans-serif`).
- `font-weight`: Text boldness (e.g., `bold`, `400`).
- `text-align`: Text alignment (e.g., `center`, `left`).

**Example**:
```css
p {
    color: #333;
    font-size: 16px;
    font-family: Arial, sans-serif;
    text-align: center;
}
```

### 2. Background Properties
- `background-color`: Background color (e.g., `blue`).
- `background-image`: Image background (e.g., `url('img.jpg')`).
- `background-repeat`: Image repeat behavior (e.g., `no-repeat`).

**Example**:
```css
body {
    background-color: #f0f0f0;
}
```

### 3. Box Model
The CSS **box model** defines how elements are sized and spaced:
- **Content**: Text or images.
- **Padding**: Space inside the border.
- **Border**: Surrounds padding.
- **Margin**: Space outside the border.

**Properties**:
- `width`/`height`: Content size (e.g., `200px`).
- `padding`: Inner spacing (e.g., `10px`).
- `border`: Border style (e.g., `1px solid black`).
- `margin`: Outer spacing (e.g., `20px`).

**Example**:
```css
div {
    width: 200px;
    padding: 10px;
    border: 1px solid gray;
    margin: 15px;
}
```

---

## CSS Layout Techniques

### 1. Display Property
Controls element rendering:
- `block`: Takes full width, new line (e.g., `<div>`).
- `inline`: Takes content width, same line (e.g., `<span>`).
- `inline-block`: Inline but respects width/height.
- `none`: Hides element.

**Example**:
```css
span {
    display: block;
}
```

### 2. Positioning
Controls element placement:
- `static`: Default, follows normal flow.
- `relative`: Offset from its normal position.
- `absolute`: Positioned relative to nearest positioned ancestor.
- `fixed`: Stays in place on scroll.

**Example**:
```css
.absolute {
    position: absolute;
    top: 10px;
    left: 20px;
}
```

### 3. Flexbox
A layout model for arranging elements in a container:
- `display: flex`: Enables flexbox.
- `flex-direction`: Sets item flow (e.g., `row`, `column`).
- `justify-content`: Aligns items horizontally (e.g., `space-between`).
- `align-items`: Aligns items vertically (e.g., `center`).

**Example**:
```css
.container {
    display: flex;
    justify-content: space-around;
    align-items: center;
}
```
```html
<div class="container">
    <div>Item 1</div>
    <div>Item 2</div>
</div>
```

---

## CSS Specificity and Cascade

The **cascade** determines which styles apply when multiple rules target the same element. **Specificity** prioritizes rules:
- Inline > ID > Class > Element.
- More specific selectors override less specific ones.

**Example**:
```css
p {
    color: blue; /* Lower specificity */
}
#special {
    color: red; /* Higher specificity */
}
```

---

## Best Practices

- Use **external CSS** for maintainability.
- Keep selectors specific but not overly complex.
- Use semantic class names (e.g., `.header` vs `.xyz`).
- Minimize inline CSS.
- Test for cross-browser compatibility.

---

## Practice Exercises

1. Style a paragraph with a custom font, color, and alignment.
2. Create a div with a border, padding, and margin.
3. Build a flexbox layout with three centered items.
4. Use an ID selector to style a unique element.