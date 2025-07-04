# Jinja2 Basics

Jinja2 is a powerful and flexible templating engine for Python, commonly used with web frameworks like Flask and Django to generate dynamic HTML content. This document provides an overview of Jinja2's core features and syntax, suitable for beginners.

## What is Jinja2?

Jinja2 is a templating library that allows developers to create dynamic web pages by embedding Python-like expressions and control structures within HTML or other text-based formats. It separates presentation logic from application logic, making it easier to maintain and update web templates.

### Key Features
- **Dynamic Content**: Injects Python variables, expressions, and logic into templates.
- **Template Inheritance**: Enables reusable layouts with blocks for customization.
- **Filters**: Modifies variables (e.g., formatting strings or numbers).
- **Control Structures**: Supports loops, conditionals, and macros for complex logic.
- **Safe Execution**: Escapes HTML to prevent security issues like XSS (cross-site scripting).

## Basic Syntax

Jinja2 uses specific delimiters to embed logic in templates:
- `{{ ... }}`: For outputting expressions or variables (e.g., `{{ username }}`).
- `{% ... %}`: For control structures like loops and conditionals (e.g., `{% if condition %}`).
- `{# ... #}`: For comments that are not rendered in the output (e.g., `{# This is a comment #}`).

### 1. Variables
Variables passed from Python (e.g., via Flask's `render_template`) can be displayed using `{{ variable }}`.

**Example**:
```html
<h1>Welcome, {{ username }}!</h1>
```
- If `username="Alice"` is passed to the template, it renders as `<h1>Welcome, Alice!</h1>`.

### 2. Filters
Filters modify variables and are applied using the pipe (`|`) operator.

**Common Filters**:
- `|upper`: Converts text to uppercase.
- `|lower`: Converts text to lowercase.
- `|default('value')`: Provides a fallback if the variable is undefined.
- `|length`: Returns the length of a list or string.

**Example**:
```html
<p>{{ username|upper }}</p>  {# Outputs "ALICE" if username="Alice" #}
<p>{{ name|default('Guest') }}</p>  {# Outputs "Guest" if name is undefined #}
```

### 3. Control Structures

#### Conditionals
Use `{% if %}` to conditionally render content.

**Example**:
```html
{% if user.logged_in %}
    <p>Welcome back, {{ user.name }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```
- Renders different content based on the `user.logged_in` boolean.

#### Loops
Use `{% for %}` to iterate over lists or dictionaries.

**Example**:
```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```
- If `items=['Apple', 'Banana', 'Orange']`, it renders a list with three `<li>` elements.

### 4. Template Inheritance
Template inheritance allows you to create a base template and extend it in child templates using `{% extends %}` and `{% block %}`.

**Base Template (`base.html`)**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

**Child Template (`child.html`)**:
```html
{% extends "base.html" %}
{% block title %}Home Page{% endblock %}
{% block content %}
    <h1>Welcome to my site!</h1>
{% endblock %}
```
- The child template inherits the structure of `base.html` and fills in the `title` and `content` blocks.

### 5. Macros
Macros are reusable template snippets, similar to functions.

**Example**:
```html
{% macro input_field(name, type='text') %}
    <input type="{{ type }}" name="{{ name }}" class="border p-2">
{% endmacro %}

{{ input_field('username') }}
{{ input_field('password', type='password') }}
```
- Defines a reusable `input_field` macro and calls it to generate input elements.

### 6. Flash Messages
In Flask, flash messages provide user feedback (e.g., success or error messages) and are accessed using `get_flashed_messages()`.

**Example**:
```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <p class="{{ 'text-red-500' if category == 'error' else 'text-green-500' }}">{{ message }}</p>
        {% endfor %}
    {% endif %}
{% endwith %}
```
- Displays messages with styling based on their category (e.g., red for errors, green for success).

### 7. URL Generation
Flask’s `url_for` function generates URLs for routes dynamically.

**Example**:
```html
<a href="{{ url_for('login') }}">Login</a>
```
- Generates a URL for the `login` route (e.g., `/login`).

## Integration with Flask
In Flask, templates are rendered using the `render_template` function, passing variables to Jinja2.

**Python (app.py)**:
```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', username='Alice', items=['Apple', 'Banana'])
```

**Template (index.html)**:
```html
<h1>Hello, {{ username }}!</h1>
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```
- Renders a page with the username and a list of items.

## Best Practices
- **Keep Templates Simple**: Avoid complex logic in templates; handle it in Python code.
- **Use Safe Filters**: Use `|safe` only when you trust the input to prevent XSS attacks.
- **Organize Templates**: Use template inheritance and macros to avoid duplication.
- **Secure Flash Messages**: Always escape user input in messages unless explicitly marked safe.

## Resources
- Official Jinja2 Documentation: [jinja.palletsprojects.com](https://jinja.palletsprojects.com)
- Flask Documentation: [flask.palletsprojects.com](https://flask.palletsprojects.com)

This overview covers the essentials of Jinja2 for creating dynamic templates in web applications.