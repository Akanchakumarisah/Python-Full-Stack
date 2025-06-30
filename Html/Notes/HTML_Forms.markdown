# HTML Forms Notes

HTML Forms are a fundamental part of web development, enabling users to input and submit data on a webpage.

---

## What Are HTML Forms?

HTML Forms allow users to interact with a webpage by entering data, such as text, selections, or files, which can then be sent to a server for processing. Common uses include login forms, search bars, and contact pages.

**Key Purposes**:
- Gather user information (e.g., name, email).
- Submit data to a server.
- Enable interactivity in web applications.

---

## Basic Form Structure

The `<form>` element is the container for all form controls. It typically includes input fields, labels, and a submit button.

**Example**:
```html
<form action="/submit" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    <input type="submit" value="Submit">
</form>
```

### `<form>` Attributes
- **`action`**: Specifies the URL where form data is sent.
- **`method`**: Defines the HTTP method for submission:
  - **`get`**: Data is appended to the URL (e.g., `/search?query=html`).
  - **`post`**: Data is sent in the request body, ideal for sensitive or large data.

---

## Form Elements

### 1. **Input Elements**
The `<input>` tag is the most versatile form element, with various types:

- **`type="text"`**: For single-line text.
  ```html
  <input type="text" name="username">
  ```
- **`type="password"`**: Masks input for security.
  ```html
  <input type="password" name="password">
  ```
- **`type="email"`**: Ensures valid email format.
  ```html
  <input type="email" name="email">
  ```
- **`type="number"`**: Restricts input to numbers.
  ```html
  <input type="number" name="age">
  ```
- **`type="checkbox"`**: Allows multiple choices.
  ```html
  <input type="checkbox" name="interests" value="coding"> Coding
  ```
- **`type="radio"`**: Limits to one choice.
  ```html
  <input type="radio" name="gender" value="male"> Male
  <input type="radio" name="gender" value="female"> Female
  ```
- **`type="file"`**: For uploading files.
  ```html
  <input type="file" name="document">
  ```
- **`type="submit"`**: Triggers form submission.
  ```html
  <input type="submit" value="Send">
  ```

### 2. **Textarea**
For multi-line text input:
```html
<textarea name="comments" rows="5" cols="40"></textarea>
```

### 3. **Select**
Creates a dropdown menu:
```html
<select name="city">
    <option value="newyork">New York</option>
    <option value="london">London</option>
</select>
```

### 4. **Buttons**
- **Submit**: Sends the form data.
  ```html
  <button type="submit">Submit</button>
  ```
- **Reset**: Clears all inputs.
  ```html
  <button type="reset">Reset</button>
  ```

---

## Labels and Accessibility

Labels improve usability and accessibility by associating text with inputs. Use the `for` attribute to link a label to an input’s `id`.

**Example**:
```html
<label for="username">Username:</label>
<input type="text" id="username" name="username">
```

---

## Form Validation

HTML5 includes built-in validation features:
- **`required`**: Makes a field mandatory.
  ```html
  <input type="text" name="name" required>
  ```

---

## Form Submission

Forms send data to the server based on the `method`:
- **GET**: Visible in the URL, suitable for non-sensitive data.
  - Example: `/submit?name=John`
- **POST**: Hidden in the request body, better for secure or large data.

---

## Best Practices

- Always pair inputs with `<label>` tags.
- Select the correct `type` for each input.
- Use `POST` for sensitive information.
- Implement validation to ensure data quality.
- Enhance accessibility with proper markup (e.g., `aria` attributes if needed).

---

## Practice Exercises

1. Build a form with fields for name, email, and a submit button.
2. Add a dropdown menu for favorite programming languages.
3. Include radio buttons for selecting a course level (e.g., beginner, advanced).
4. Test the form with both `GET` and `POST` methods.