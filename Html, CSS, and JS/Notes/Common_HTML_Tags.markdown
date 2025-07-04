# Commonly Used HTML Tags Notes

HTML (Hypertext Markup Language) uses **tags** to define the structure and content of webpages. This document lists the most commonly used HTML tags, including text formatting, semantic, and interactive elements, with their purposes and examples.

---

## Document Structure Tags

These tags define the overall structure of an HTML document.

- `<!DOCTYPE html>`: Declares the document as HTML5.

  ```html
  <!DOCTYPE html>
  ```

- `<html>`: Root element of the webpage.

  ```html
  <html lang="en">
  </html>
  ```

- `<head>`: Contains metadata (e.g., title, character set).

  ```html
  <head>
      <title>My Page</title>
  </head>
  ```

- `<body>`: Holds visible content.

  ```html
  <body>
      <h1>Hello</h1>
  </body>
  ```

- `<title>`: Sets the webpage’s title (shown in browser tab).

  ```html
  <title>My Website</title>
  ```

- `<meta>`: Provides metadata (e.g., charset, viewport).

  ```html
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  ```

---

## Semantic Tags

Semantic tags describe the meaning of content, improving accessibility and SEO.

- `<header>`: Defines a header section.

  ```html
  <header>
      <h1>Site Title</h1>
  </header>
  ```

- `<nav>`: Contains navigation links.

  ```html
  <nav>
      <a href="#home">Home</a>
  </nav>
  ```

- `<main>`: Represents the main content.

  ```html
  <main>
      <p>Main content here.</p>
  </main>
  ```

- `<section>`: Groups related content.

  ```html
  <section>
      <h2>About Us</h2>
  </section>
  ```

- `<article>`: Represents standalone content (e.g., a blog post).

  ```html
  <article>
      <h2>Blog Post</h2>
  </article>
  ```

- `<footer>`: Defines a footer section.

  ```html
  <footer>
      <p>© 2025</p>
  </footer>
  ```

- `<figure>`: Wraps media (e.g., images) with a caption.

  ```html
  <figure>
      <img src="photo.jpg" alt="Scenery">
      <figcaption>Beautiful landscape</figcaption>
  </figure>
  ```

---

## Text Formatting Tags

These tags format text for styling or semantic purposes.

- `<h1>` **to** `<h6>`: Headings, from largest (`<h1>`) to smallest (`<h6>`).

  ```html
  <h1>Main Heading</h1>
  <h3>Subheading</h3>
  ```

- `<p>`: Defines a paragraph.

  ```html
  <p>This is a paragraph.</p>
  ```

- `<strong>`: Bold text with semantic emphasis (important).

  ```html
  <strong>Important text</strong>
  ```

- `<em>`: Italic text with semantic emphasis (stress).

  ```html
  <em>Emphasized text</em>
  ```

- `<b>`: Bold text (visual, not semantic).

  ```html
  <b>Bold text</b>
  ```

- `<i>`: Italic text (visual, not semantic).

  ```html
  <i>Italic text</i>
  ```

- `<u>`: Underlined text (use sparingly, prefer CSS).

  ```html
  <u>Underlined text</u>
  ```

- `<sup>`: Superscript text (e.g., for exponents).

  ```html
  E = mc<sup>2</sup>
  ```

- `<sub>`: Subscript text (e.g., for chemical formulas).

  ```html
  H<sub>2</sub>O
  ```

- `<code>`: Displays inline code snippets.

  ```html
  Use <code>print("Hello")</code> in Python.
  ```

- `<pre>`: Displays preformatted text (preserves spaces and line breaks).

  ```html
  <pre>
  function hello() {
      console.log("Hello, World!");
  }
  </pre>
  ```

- `<blockquote>`: Indicates a quoted section.

  ```html
  <blockquote cite="https://example.com">
      This is a quote.
  </blockquote>
  ```

- `<br>`: Inserts a line break (self-closing).

  ```html
  Line one<br>Line two
  ```

- `<hr>`: Adds a horizontal rule (self-closing).

  ```html
  <hr>
  ```

---

## Links and Media Tags

These tags add links and multimedia content.

- `<a>`: Creates a hyperlink.

  ```html
  <a href="https://example.com">Visit Example</a>
  ```

- `<img>`: Embeds an image (self-closing).

  ```html
  <img src="image.jpg" alt="Description">
  ```

- `<audio>`: Embeds audio content.

  ```html
  <audio controls>
      <source src="audio.mp3" type="audio/mpeg">
  </audio>
  ```

- `<video>`: Embeds video content.

  ```html
  <video controls width="400">
      <source src="video.mp4" type="video/mp4">
  </video>
  ```

---

## List Tags

These tags create ordered or unordered lists.

- `<ul>`: Unordered (bulleted) list.

  ```html
  <ul>
      <li>Item 1</li>
      <li>Item 2</li>
  </ul>
  ```

- `<ol>`: Ordered (numbered) list.

  ```html
  <ol>
      <li>First</li>
      <li>Second</li>
  </ol>
  ```

- `<li>`: List item within `<ul>` or `<ol>`.

  ```html
  <li>List item</li>
  ```

---

## Form Tags

These tags create interactive forms.

- `<form>`: Container for form elements.

  ```html
  <form action="/submit" method="post">
      <!-- Form controls -->
  </form>
  ```

- `<input>`: Input field (e.g., text, checkbox).

  ```html
  <input type="text" name="username">
  <input type="submit" value="Send">
  ```

- `<label>`: Associates text with a form control.

  ```html
  <label for="name">Name:</label>
  <input type="text" id="name" name="name">
  ```

- `<textarea>`: Multi-line text input.

  ```html
  <textarea name="comments" rows="4" cols="50"></textarea>
  ```

- `<select>`: Dropdown menu.

  ```html
  <select name="option">
      <option value="1">Option 1</option>
      <option value="2">Option 2</option>
  </select>
  ```

- `<button>`: Clickable button.

  ```html
  <button type="submit">Submit</button>
  ```

---

## Table Tags

These tags create tabular data.

- `<table>`: Defines a table.

  ```html
  <table>
      <!-- Rows and cells -->
  </table>
  ```

- `<tr>`: Table row.

  ```html
  <tr>
      <td>Cell</td>
  </tr>
  ```

- `<th>`: Table header cell.

  ```html
  <th>Header</th>
  ```

- `<td>`: Table data cell.

  ```html
  <td>Data</td>
  ```

---

## Generic Container Tags

These tags group content for styling or scripting.

- `<div>`: Block-level container.

  ```html
  <div class="container">
      <p>Content</p>
  </div>
  ```

- `<span>`: Inline container.

  ```html
  <span class="highlight">Text</span>
  ```

---

## Best Practices

- Prefer **semantic tags** (e.g., `<strong>`, `<em>`) over visual tags (e.g., `<b>`, `<i>`) for accessibility.
- Use `<u>` sparingly; prefer CSS for underlines.
- Always include `alt` attributes for `<img>` tags.
- Pair `<label>` with `<input>` for form accessibility.
- Use lowercase for tag names.
- Ensure all tags are properly closed.

---

## Practice Exercises

1. Create a webpage with `<header>`, `<nav>`, `<main>`, and `<footer>` sections, using `<strong>` and `<em>` for emphasis.
2. Build a form with `<input>`, `<textarea>`, `<select>`, and `<button>`, including `<sup>` for a footnote reference.
3. Design a table with `<th>` and `<td>`, and use `<sub>` to denote a chemical formula in one cell.
4. Embed an `<img>` and `<video>`, and add a `<blockquote>` with a `<figure>` for a captioned image.