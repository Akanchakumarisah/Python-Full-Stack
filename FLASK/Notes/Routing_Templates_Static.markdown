# Flask Routing, Templates, and Static Files

## 1. Routing

Routing in Flask maps URLs to Python functions (view functions) using the `@app.route` decorator. It defines how the application responds to client requests for specific endpoints. Routes can include dynamic URL components and support multiple HTTP methods.

**Key Features**:
- Supports static and dynamic routes (e.g., `/user/<name>`).
- Handles HTTP methods like GET, POST, etc.
- Uses `url_for` to generate URLs dynamically.

**Example**:

```python
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'

@app.route('/post/<int:id>', methods=['GET'])
def post(id):
    return f'Post ID: {id}'
```

**Explanation**:
- `/` is a static route for the home page.
- `/user/<name>` is a dynamic route accepting a string parameter.
- `/post/<int:id>` accepts an integer parameter and specifies the GET method.

## 2. Templates

Templates in Flask are HTML files rendered dynamically using the `render_template` function. They are typically stored in a `templates` folder and use Jinja2 for templating, allowing dynamic content insertion, loops, and conditionals.

**Key Features**:
- Uses Jinja2 syntax (e.g., `{{ variable }}` for variables, `{% for %}` for loops).
- Supports template inheritance for reusable layouts.
- Renders dynamic data passed from view functions.

**Example**:

**Python Code**:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)
```

**HTML Template (templates/profile.html)**:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Profile</title>
</head>
<body>
    <h1>Welcome, {{ username }}!</h1>
    <p>This is your profile page.</p>
</body>
</html>
```

**Explanation**:
- The `profile` function passes `username` to `render_template`.
- The template uses `{{ username }}` to display the dynamic value.
- Templates must be stored in a `templates` folder in the project directory.

## 3. Static Files

Static files in Flask (e.g., CSS, JavaScript, images) are served from a `static` folder. They are accessed via the `/static` URL path and are used to enhance the appearance and functionality of templates.

**Key Features**:
- Common file types: `.css`, `.js`, `.png`, `.jpg`, etc.
- Accessed in templates using `url_for('static', filename='file')`.
- No server-side processing; served directly to the client.

**Example**:

**Python Code**:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```

**HTML Template (templates/index.html)**:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Welcome to My Site</h1>
    <img src="{{ url_for('static', filename='logo.png') }}" alt="Logo">
    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
```

**CSS File (static/styles.css)**:

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}
h1 {
    color: #333;
}
```

**JavaScript File (static/script.js)**:

```javascript
console.log("Static JavaScript file loaded!");
```

**Explanation**:
- The `static` folder contains `styles.css`, `script.js`, and `logo.png`.
- `url_for('static', filename='styles.css')` generates the correct path to the static file.
- Static files enhance the template's styling and interactivity.

## Project Structure

A typical Flask project structure for routing, templates, and static files:

```
project/
├── app.py
├── templates/
│   ├── index.html
│   ├── profile.html
├── static/
│   ├── styles.css
│   ├── script.js
│   ├── logo.png
```

## Notes
- Ensure the `templates` and `static` folders are in the same directory as your Flask app.
- Use `url_for` to avoid hard-coding URLs for routes and static files.
- Jinja2 supports advanced features like template inheritance and filters for complex templates.