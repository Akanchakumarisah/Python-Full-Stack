# Flask Web Development Notes

## Setting up Flask Environment

Flask is a lightweight Python web framework. To set up a Flask environment, you need Python installed and a virtual environment to manage dependencies.

### Steps to Set Up:
1. **Install Python**: Ensure Python 3.6+ is installed.
2. **Create a Virtual Environment**:
   - Run `python -m venv venv` to create a virtual environment named `venv`.
   - Activate it:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`
3. **Install Flask**:
   - Run `pip install flask` to install Flask.
4. **Verify Installation**:
   - Create a simple Flask app to test:
     ```python
     from flask import Flask
     app = Flask(__name__)

     @app.route('/')
     def hello():
         return 'Hello, Flask!'
     ```
   - Save as `app.py` and run with `flask run` (ensure `FLASK_APP=app.py` is set).
   - Visit `http://127.0.0.1:5000` in a browser.

### Example:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask
```

## Routing, Templates, and Static Files

Flask uses **routing** to map URLs to Python functions, **templates** for dynamic HTML, and **static files** for assets like CSS and JavaScript.

### Routing:
- Define routes using the `@app.route()` decorator.
- Example:
  ```python
  @app.route('/')
  def home():
      return 'Welcome to the Home Page!'
  @app.route('/about')
  def about():
      return 'About Us'
  ```

### Templates:
- Use Jinja2 for rendering HTML templates.
- Store templates in a `templates` folder.
- Example (`templates/index.html`):
  ```html
  <!DOCTYPE html>
  <html>
  <head><title>Home</title></head>
  <body><h1>Welcome, {{ name }}!</h1></body>
  </html>
  ```
- Render in Python:
  ```python
  from flask import render_template
  @app.route('/user/<name>')
  def user(name):
      return render_template('index.html', name=name)
  ```

### Static Files:
- Store CSS, JavaScript, and images in a `static` folder.
- Access via `/static/<filename>` (e.g., `/static/style.css`).
- Example (`static/style.css`):
  ```css
  h1 { color: navy; }
  ```

## Handling GET/POST Requests

Flask handles HTTP methods like GET and POST to process user input.

### GET Requests:
- Used to retrieve data, often via URL parameters.
- Example:
  ```python
  @app.route('/greet/<name>')
  def greet(name):
      return f'Hello, {name}!'
  ```
- URL: `http://127.0.0.1:5000/greet/Alice` → Output: `Hello, Alice!`

### POST Requests:
- Used to submit data (e.g., forms).
- Specify methods in the route:
  ```python
  from flask import request
  @app.route('/submit', methods=['POST'])
  def submit():
      data = request.form['username']
      return f'Submitted: {data}'
  ```
- Example form (`templates/form.html`):
  ```html
  <form method="POST" action="/submit">
      <input type="text" name="username">
      <input type="submit" value="Submit">
  </form>
  ```

## Hands-On: Simple Flask App with Form Submission

Create a Flask app with a form that accepts a username and displays a greeting.

### Example Code:
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    return render_template('result.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
```

### Templates:
- `templates/form.html`:
  ```html
  <!DOCTYPE html>
  <html>
  <head><title>Form</title></head>
  <body>
      <form method="POST" action="/submit">
          <label>Username:</label>
          <input type="text" name="username">
          <input type="submit" value="Submit">
      </form>
  </body>
  </html>
  ```
- `templates/result.html`:
  ```html
  <!DOCTYPE html>
  <html>
  <head><title>Result</title></head>
  <body><h1>Hello, {{ username }}!</h1></body>
  </html>
  ```

### Running:
- Run `flask run` and visit `http://127.0.0.1:5000`.
- Enter a username, submit, and see the greeting.

## Rendering Dynamic HTML Templates

Jinja2 allows dynamic content in templates using variables, loops, and conditionals.

### Variables:
- Pass data to templates via `render_template`:
  ```python
  @app.route('/profile/<name>')
  def profile(name):
      return render_template('profile.html', name=name, age=25)
  ```
- Template (`templates/profile.html`):
  ```html
  <h1>Profile: {{ name }}</h1>
  <p>Age: {{ age }}</p>
  ```

### Loops and Conditionals:
- Example:
  ```python
  @app.route('/users')
  def users():
      user_list = ['Alice', 'Bob', 'Charlie']
      return render_template('users.html', users=user_list)
  ```
- Template (`templates/users.html`):
  ```html
  <ul>
  {% for user in users %}
      <li>{{ user }}</li>
  {% endfor %}
  </ul>
  {% if users %}
      <p>Users found!</p>
  {% else %}
      <p>No users found.</p>
  {% endif %}
  ```

## Form Validation and User Input Handling

Validate user input to ensure data integrity and security.

### Using `request.form`:
- Access form data and validate:
  ```python
  @app.route('/register', methods=['POST'])
  def register():
      username = request.form.get('username')
      if not username or len(username) < 3:
          return 'Username must be at least 3 characters!', 400
      return f'Registered: {username}'
  ```

### Using WTForms (Optional):
- Install: `pip install flask-wtf`
- Example:
  ```python
  from flask_wtf import FlaskForm
  from wtforms import StringField, SubmitField
  from wtforms.validators import DataRequired, Length

  class RegistrationForm(FlaskForm):
      username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
      submit = SubmitField('Register')
  ```
- Route:
  ```python
  from flask import render_template, flash
  @app.route('/register', methods=['GET', 'POST'])
  def register():
      form = RegistrationForm()
      if form.validate_on_submit():
          flash(f'Registered {form.username.data}!')
          return redirect('/')
      return render_template('register.html', form=form)
  ```
- Template (`templates/register.html`):
  ```html
  <form method="POST">
      {{ form.hidden_tag() }}
      {{ form.username.label }} {{ form.username() }}
      {{ form.submit() }}
  </form>
  ```

## Connecting CSS/JavaScript to Flask

Enhance Flask apps with CSS and JavaScript for styling and interactivity.

### CSS:
- Store in `static/style.css`:
  ```css
  body {
      font-family: Arial, sans-serif;
      background-color: #f0f0f0;
  }
  .container {
      text-align: center;
      margin-top: 50px;
  }
  ```
- Link in template:
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```

### JavaScript:
- Store in `static/script.js`:
  ```javascript
  document.addEventListener('DOMContentLoaded', () => {
      alert('Welcome to the Flask App!');
  });
  ```
- Link in template:
  ```html
  <script src="{{ url_for('static', filename='script.js') }}"></script>
  ```

### Example Template:
- `templates/index.html`:
  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <title>Home</title>
      <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  </head>
  <body>
      <div class="container">
          <h1>Welcome to Flask!</h1>
      </div>
      <script src="{{ url_for('static', filename='script.js') }}"></script>
  </body>
  </html>
  ```