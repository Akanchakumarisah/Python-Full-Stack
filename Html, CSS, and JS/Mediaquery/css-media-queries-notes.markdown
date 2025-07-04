# CSS Media Queries Notes

## Media Query

**Media Queries** are a CSS feature that allows you to apply styles based on the characteristics of the user's device, such as screen size, resolution, orientation, or other environmental conditions. They are a cornerstone of responsive web design, enabling websites to adapt to various devices like desktops, tablets, and smartphones.

### Explanation
- **Syntax**: `@media [media-type] and (media-feature) { /* styles */ }`
- **Media Types**: Common types include `all` (default), `screen`, `print`, and `speech`.
- **Media Features**: Conditions like `min-width`, `max-width`, `orientation`, `resolution`, etc.
- **Purpose**: Adjusts layout, typography, or other styles to optimize user experience across devices.
- **Breakpoints**: Specific screen sizes (e.g., 768px for tablets, 1200px for desktops) where styles change.
- **Pros**: Enables responsive and adaptive design, improves accessibility, and supports device-specific styling.
- **Cons**: Overuse can lead to complex CSS; requires testing across devices.

**Example**:
```css
/* Default styles */
.container {
    background-color: lightblue;
    padding: 20px;
}

/* Apply styles for screens smaller than 600px */
@media screen and (max-width: 600px) {
    .container {
        background-color: lightgreen;
        padding: 10px;
    }
}
```

**HTML**:
```html
<div class="container">This is a responsive container.</div>
```

In this example, the container’s background changes from light blue to light green on screens narrower than 600px.

---

## Example of Media Query

Below is a detailed example demonstrating media queries for different screen sizes and orientations.

**Example**:
```css
/* Default styles for all devices */
body {
    font-family: Arial, sans-serif;
    font-size: 16px;
}

.header {
    background-color: #333;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Styles for tablets (screens between 600px and 900px) */
@media screen and (min-width: 600px) and (max-width: 900px) {
    .header {
        background-color: #0066cc;
        font-size: 1.2em;
    }
}

/* Styles for mobile devices in portrait mode (max-width 600px) */
@media screen and (max-width: 600px) and (orientation: portrait) {
    .header {
        background-color: #cc3300;
        font-size: 1em;
        padding: 10px;
    }
}

/* Styles for high-resolution screens */
@media screen and (min-resolution: 192dpi) {
    .header {
        font-weight: bold;
    }
}
```

**HTML**:
```html
<div class="header">Welcome to My Website</div>
```

**Explanation**:
- On screens wider than 900px, the header has a dark background and default styles.
- On tablets (600px–900px), the header turns blue with a larger font.
- On mobile devices in portrait mode (≤600px), the header turns red with smaller padding.
- On high-resolution screens (≥192dpi), the header text becomes bold.

---

## Use-Case

Media queries are used in various scenarios to enhance user experience and ensure compatibility across devices. Below are common use cases with examples.

### 1. Responsive Layouts
Adjust layouts (e.g., grid to single-column) for different screen sizes.

**Example**:
```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

@media screen and (max-width: 768px) {
    .container {
        grid-template-columns: 1fr; /* Single column on smaller screens */
    }
}
```

**HTML**:
```html
<div class="container">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
</div>
```

**Use Case**: A product gallery displays in a three-column grid on desktops but switches to a single-column layout on mobile devices for better readability.

### 2. Adjusting Typography
Modify font sizes or line heights for legibility on smaller screens.

**Example**:
```css
p {
    font-size: 18px;
    line-height: 1.6;
}

@media screen and (max-width: 600px) {
    p {
        font-size: 14px;
        line-height: 1.4;
    }
}
```

**HTML**:
```html
<p>This is a paragraph with responsive text sizing.</p>
```

**Use Case**: Ensures text remains readable on small screens without excessive zooming.

### 3. Hiding/Showing Elements
Show or hide elements based on device capabilities or screen size.

**Example**:
```css
.desktop-only {
    display: block;
}

.mobile-only {
    display: none;
}

@media screen and (max-width: 600px) {
    .desktop-only {
        display: none;
    }
    .mobile-only {
        display: block;
    }
}
```

**HTML**:
```html
<div class="desktop-only">Visible on desktop</div>
<div class="mobile-only">Visible on mobile</div>
```

**Use Case**: Display a simplified navigation menu on mobile devices while showing a full menu on desktops.

### 4. Orientation-Based Styling
Apply styles based on device orientation (portrait or landscape).

**Example**:
```css
.image {
    width: 100%;
    height: auto;
}

@media screen and (orientation: landscape) {
    .image {
        width: 50%;
        float: left;
        margin-right: 20px;
    }
}
```

**HTML**:
```html
<img class="image" src="example.jpg" alt="Responsive Image">
```

**Use Case**: Adjusts image layout for better use of space in landscape mode on mobile devices.

### 5. Print Styles
Customize styles for printing a webpage.

**Example**:
```css
body {
    background-color: #f0f0f0;
}

@media print {
    body {
        background-color: white;
        color: black;
    }
    .no-print {
        display: none;
    }
}
```

**HTML**:
```html
<div class="no-print">This won't print!</div>
<p>This will print in black on white.</p>
```

**Use Case**: Ensures printed pages are clean, removing unnecessary elements like ads or navigation bars.