# HTML5 Notes

**HTML5** (Hypertext Markup Language, version 5) is the standard language for creating web pages. It defines the structure and content of a webpage, which is then styled with CSS and made interactive with JavaScript.

---

## What is HTML?

HTML is a **markup language** used to create the structure of web pages. It uses **elements** defined by **tags** (enclosed in `< >`) to represent different parts of a webpage, such as headings, paragraphs, and images.

**Example**:
```html
<h1>Hello, World!</h1>
<p>This is a paragraph.</p>
```

---

## Basic Structure of an HTML5 Document

Every HTML5 document follows this structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Page</title>
</head>
<body>
    <!-- Content goes here -->
</body>
</html>
```

### Key Parts:
- **`<!DOCTYPE html>`**: Declares the document as HTML5.
- **`<html>`**: The root element.
- **`<head>`**: Contains metadata (e.g., title, character set).
- **`<body>`**: Holds the visible content.

---

## HTML Elements and Tags

Elements are defined by **tags**, usually in pairs:
- **Opening tag**: `<tagname>`
- **Closing tag**: `</tagname>`

Some tags are **self-closing** (e.g., `<img>`).

**Examples**:
- `<h1>Heading</h1>`: A heading.
- `<p>Text here.</p>`: A paragraph.
- `<img src="pic.jpg" alt="A picture">`: An image.

---

## Common HTML Elements

### Headings
Six levels: `<h1>` (largest) to `<h6>` (smallest).
```html
<h1>Big Heading</h1>
<h2>Smaller Heading</h2>
```

### Paragraphs
```html
<p>This is some text.</p>
```

### Links
Use `<a>` with an `href` attribute.
```html
<a href="https://example.com">Click Me</a>
```

### Images
Use `<img>` with `src` and `alt` attributes.
**Relative File Path :** The file location with respect to the current folder.
**Absolute File Path :** The complete file location from the root directory.
**Specifying URL's :** Use the full URL to link to an image hosted online.

```html
<img src="image.jpg" alt="Image description">
```

### Lists
- **Unordered (`<ul>`)**:
```html
<ul>
    <li>Apple</li>
    <li>Banana</li>
</ul>
```
- **Ordered (`<ol>`)**:
```html
<ol>
    <li>First</li>
    <li>Second</li>
</ol>
```

---

## Attributes

Attributes add details to elements, written as name-value pairs in the opening tag.

**Examples**:
- `id="unique"`: Unique identifier.
- `class="group"`: For styling or scripting.
- `src="file.jpg"`: Source for images.

```html
<img src="logo.png" alt="Logo" id="main-logo">
```

---

## Block vs. Inline Elements

- **Block-level**: Takes full width, starts on a new line (e.g., `<div>`, `<p>`).
- **Inline**: Takes only needed width, stays on the same line (e.g., `<span>`, `<a>`).

**Example**:
```html
<p>Block text</p>
<span>Inline text</span>
```

---

## HTML5 Semantic Elements

Semantic elements give meaning to the structure:
- `<header>`: Page or section header.
- `<footer>`: Page or section footer.
- `<nav>`: Navigation links.
- `<article>`: Standalone content.
- `<section>`: Thematic section.

**Example**:
```html
<header>
    <h1>My Site</h1>
</header>
<nav>
    <a href="#home">Home</a>
</nav>
<section>
    <p>Welcome!</p>
</section>
```

---

## Forms in HTML5

Forms collect user input using `<form>` and input elements.

**Example**:
```html
<form action="/submit" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    <input type="submit" value="Send">
</form>
```

### Input Types
- `text`: Text field.
- `password`: Hidden text.
- `email`: Email field.
- `submit`: Submit button.

---

## Multimedia in HTML5

### Audio
```html
<audio controls>
    <source src="sound.mp3" type="audio/mpeg">
</audio>
```

### Video
```html
<video controls width="400">
    <source src="movie.mp4" type="video/mp4">
</video>
```

---

## Tables

Tables use `<table>`, `<tr>` (row), `<th>` (header), and `<td>` (data).

**Example**:
```html
<table>
    <tr>
        <th>Name</th>
        <th>Age</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>20</td>
    </tr>
</table>
```

---

## Best Practices

- Use semantic elements.
- Close all tags.
- Use lowercase for tags.
- Add `alt` text to images.

---

## Exercises

1. Create a page with a heading, paragraph, and image.
2. Build a form with name and email fields.
3. Embed a video or audio file.
4. Make a table with 2 rows and 2 columns.
---