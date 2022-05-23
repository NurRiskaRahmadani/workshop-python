# PEMROGRAMAN WEB - FLASK (Pertemuan 11)
## A. Teori
Flask merupakan sebuah web framework yang ditulis dalam bahasa Python dan tergolong kedalam jenis microframework. Berfungsi sebagai kerangka kerja aplikasi dan tampian dari suatu web. Dengan menggunakan flask serta bahasa Python, seorang pengembang dapat membuat sebuah web yang terstruktur dan dapat mengatur behaviour.

## B. Flask
Pastikan untuk membuat *environment* baru untuk *project* yang akan dibuat agar dapat menyediakan *space* tersendiri, sehingga tidak bersinggungan dengan *environment* utama yakni *base* milik user. 

1. Buat *environment* 
Jalankan perintah berikut untuk membuat *environment* baru :
```
(flask-practice) C:\Users\Riska\flask-tutorial>conda create --name flask-practice
```

2. Aktifkan *environment*
Setelah *environment*, lakukan peng-aktifan *environment* agar dapat digunakan. Berikut ini merupakan perintah untuk mengaktifkan *environment* :
```
(flask-practice) C:\Users\Riska\flask-tutorial>conda activate flask-practice
```

3. Instalasi Flask
Lakukan penginstalan modul flask agar dapat digunakan pada *environment* yang dibuat. Jalankan perintah berikut ini :
```
(flask-practice) C:\Users\Riska\flask-tutorial>conda install flask
```

4. Instalasi selesai

### a. Project Layout
1. Membuat directory
```
(flask-practice) C:\Users\Riska\flask-tutorial>mkdir flask-tutorial
(flask-practice) C:\Users\Riska\flask-tutorial>cd flask-tutorial
```

2. Membuat *single file flask*
Berikut ini merupakan *single file* yang dibuat pada *directory* flask-tutorial. 
```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
``` 

3. *Directory* yang akan digunakan pada *project* ini :
```
/home/Users/Riska/workshop-python/src/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

.gitignore :
```
*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/
```

### b. Application Setup
#### The Application Factory
1. Membuat *directory* flaskr

```python
$ mkdir flaskr
$ cd flaskr
```

2. Menyiapkan file __init__.py

flaskr/__init__.py
```python
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

3. *Running* Aplikasi
Menjalankan perintah berikut untuk melihat aplikasi yang telah di deploy :
```
(flask-practice) C:\Users\Riska\flask-tutorial>set FLASK_APP=flaskr
(flask-practice) C:\Users\Riska\flask-tutorial>set FLASK_ENV=development
(flask-practice) C:\Users\Riska\flask-tutorial>flask run
```

Setelah dijalankan, user akan mendapat output seperti berikut ini :
```
* Serving Flask app 'flaskr' (lazy loading)
* Environment: development
* Debug mode: on
* Restarting with stat
* Debugger is active!
* Debugger PIN: 674-445-017
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### c. Define and Access the Database
#### 1. Connect to the Database
Menambahkan file baru pada *directory* flaskr yang diberi nama **db.py** . 

flaskr/db.py
```python
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
```

#### 2. Create the tables
Menambahkan file baru pada *directory* flaskr yang diberi nama **schema.sql** . 

flaskr/schema.sql 
```sql
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```

Setelah file **schema.sql** dibuat, tambahkan beberapa *command* baru pada file **db.py** agar dapat menjalankan *SQL command* nya. 

Berikut ini merupakan *command* tambahannya :
```python
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```

#### 3. Register with the Application
Kembali menambahkan *command* baru pada file **db.py** serta beberapa *command* pada file **__init__.py**. 

flaskr/db.py
```python
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

flaskr/__init__.py
```python
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```

#### 4. Intialize the Database File
Menjalankan perintah berikut untuk menginisialisasikan database yang dibuat :

```
(flask-practice) C:\Users\Riska\flask-tutorial> flask init-db
Initialized the database
```

### d. Blueprints and Views

#### 1. Create a Blueprint
Menambahkan file baru pada *directory* flaskr yang diberi nama **auth.py** dan juga menambahkan beberapa *command* baru pada file **__init__.py**. 

flaskr/auth.py
```python
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
```

flaskr/__init__.py
```python
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app
```

#### 2. The First View : Register
Menambahkan beberapa *command* baru pada file **auth.py** agar dapat menambahkan opsi register, login dan juga logout pada aplikasi yang dibuat.

flaskr/auth.py - register
```python
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
``` 

flaskr/auth.py - login
```python
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```

flaskr/auth.py - login
```python
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```

flaskr/auth.py - Request
```python
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
```

flaskr/auth.py - logout
```python
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```

#### 3. Require Authentication in Other Views
Menambahkan beberapa *command* baru pada file **auth.py** agar dapat menambahkan dekorasi baru pada aplikasi yang dibuat.

flaskr/auth.py 
```python
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```

#### 4. Endpoints and URLs
*Function* url_for() akan menghasilkan URL ke tampilan *web-view* berdasarkan nama dan juga argumen. Nama yang berada pada URL tersebut yang dinamakan *endpoints*, dan secara *default* akan memiliki fungsi yang sama dengan nama tampilan. 

### e. Templates
*Template* merupakan file yang berisi data statis serta *placeholder* untuk data dinamis. Sebuah *template* akan diberikan dengan beberapa data tertentu sehingga menghasilkan dokumen akhir. Flask menggunakan *library* Jinja sebagai *template* nya. 

Jinja terlihat dan tampak serupa dengan Python. Terdapat pembatas khusus pada Jinja yang dapat digunakan untuk membedakan sintaks Jinja dari data statis didalam *template*

#### 1. The Base Layout
Setiap laman pada sebuah aplikasi akan memiliki *base layout* yang sama pada beberapa bagian dengan *body* yang sedikit berbeda. 

Berikut ini merupakan *base layout* yang akan diterapkan kedalam file **base.html** didalam *directory* flaskr.

flaskr/templates/base.html
```html
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>
```


#### 2. Register
flaskr/templates/auth/register.html
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```

#### 3. Log In
flaskr/templates/auth/login.html
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Log In{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Log In">
  </form>
{% endblock %}
```

#### 4. Register A User
Setelah *template* berhasil dibuat dan diterapkan kedalam program aplikasi, user dapat mulai menguji tampilan untuk register sebagai pengguna dengan menjalankan perintah _flask run_ yang mana akan menunjukkan URL : http://127.0.0.1:5000/auth/register. 

### f. Static Files
Tampilan serta *template* autentikasi akan berfungsi, walaupun mungkin akan terlihat sederhana saat ini. Maka itu penambahan beberapa file dalam bentuk CSS akan dibuat untuk memperindah tampilan html pada aplikasi yang dibuat. Gaya dari tampilan file ini akan berupa tampilan statis dan bukan *template* lagi. 

Flask akan secara otomatis menambahkan *command* static untuk mengatur tampilan melalui *directory* yang ada. 

flaskr/static/style.css
```css
html { 
    font-family: sans-serif; 
    background: #eee; 
    padding: 1rem; 
}
body { 
    max-width: 960px; 
    margin: 0 auto; 
    background: white;
}
h1 { 
    font-family: serif; 
    color: #377ba8; 
    margin: 1rem 0; 
}
a { 
    color: #377ba8; 
}
hr { 
    border: none; 
    border-top: 1px solid lightgray; 
}
nav { 
    background: lightgray; 
    display: flex; 
    align-items: center; 
    padding: 0 0.5rem; 
}
nav h1 { 
    flex: auto; 
    margin: 0; 
}
nav h1 a { 
    text-decoration: none; 
    padding: 0.25rem 0.5rem; 
}
nav ul  { 
    display: flex; 
    list-style: none; 
    margin: 0; 
    padding: 0; 
}
nav ul li a, nav ul li span, header .action { 
    display: block; 
    padding: 0.5rem; 
}
.content 
{
    padding: 0 1rem 1rem; 
}
.content > header 
{ 
    border-bottom: 1px solid lightgray; 
    display: flex; 
    align-items: flex-end; 
}
.content > header h1 
{ 
    flex: auto; 
    margin: 1rem 0 0.25rem 0; 
}
.flash {
     margin: 1em 0; 
    padding: 1em; 
    background: #cae6f6; 
    border: 1px solid #377ba8;
 }
.post > header { 
    display: flex; 
    align-items: flex-end; 
    font-size: 0.85em;
}
.post > header > div:first-of-type 
{ 
    flex: auto; 
}
.post > header h1 { 
    font-size: 1.5em;
    margin-bottom: 0; 
}
.post .about { 
    color: slategray; 
    font-style: italic; 
}
.post .body { 
    white-space: pre-line; 
}
.content:last-child { 
    margin-bottom: 0; 
}
.content form { 
    margin: 1em 0; 
    display: flex; 
    flex-direction: column; 
}
.content label { 
    font-weight: bold; 
    margin-bottom: 0.5em; 
}
.content input, .content textarea { 
    margin-bottom: 1em; 
}
.content textarea { 
    min-height: 12em; 
    resize: vertical; 
}
input.danger { 
    color: #cc2f2e; 
}
input[type=submit] { 
    align-self: start; min-width: 10em; 
}
```

### g. Blog Blueprint
#### 1. The Blueprint

flaskr/blog.py
```python
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
```

flaskr/_init__.py
```
def create_app():
    app = ...
    # existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```

#### 2. Index
flaskr/blog.py
```python
@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
```

flaskr/templates/blog/index.html
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Posts{% endblock %}</h1>
  {% if g.user %}
    <a class="action" href="{{ url_for('blog.create') }}">New</a>
  {% endif %}
{% endblock %}

{% block content %}
  {% for post in posts %}
    <article class="post">
      <header>
        <div>
          <h1>{{ post['title'] }}</h1>
          <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
        </div>
        {% if g.user['id'] == post['author_id'] %}
          <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
        {% endif %}
      </header>
      <p class="body">{{ post['body'] }}</p>
    </article>
    {% if not loop.last %}
      <hr>
    {% endif %}
  {% endfor %}
{% endblock %}
```

#### 3. Create
flaskr/blog.py
```python
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
```

flaskr/templates/blog/create.html
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}New Post{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title" value="{{ request.form['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
{% endblock %}
```

#### 4. Update
flaskr/blog.py
```python
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
```

```python
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```

flaskr/templates/blod/update.html
```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Edit "{{ post['title'] }}"{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title"
      value="{{ request.form['title'] or post['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
  <hr>
  <form action="{{ url_for('blog.delete', id=post['id']) }}" method="post">
    <input class="danger" type="submit" value="Delete" onclick="return confirm('Are you sure?');">
  </form>
{% endblock %}
```

#### 5. Delete
flaskr/blog.py
```python
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
```

### h. Make the Project Installable
#### 1. Describe the Project
Membuat file baru bernama **setup.py** untuk mendeskripsikan project dan file yang dibuat serta membuat file **MANIFEST.in**.

setup.py 
```python
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
```

MANIFEST.in
```
include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

#### 2. Install the Project
Menggunakan perintah _pip_ untuk menginstal project pada *virtual environment*.

```
(flask-practice) C:\Users\Riska\flask-tutorial>pip install -e .
```

Lalu menjalankan perintah _pip list_ untuk melihat dan mengobservasi pip yang telah diinstal. 
```
(flask-practice) C:\Users\Riska\flask-tutorial>pip list

Package        Version   Location
-------------- --------- ----------------------------------
certifi        2022.5.18.1
click          8.0.4
colorama       0.4.4
Flask          2.0.3
flaskr         1.0.0     c:\users\riska\flask-tutorial
itsdangerous   2.0.1
Jinja2         3.0.3
MarkupSafe     2.0.1
pip            21.2.4
setuptools     61.2.0
Werkzeug       2.0.3
wheel          0.37.1
wincertstore   0.2 
```

### i. Test Coverage

Meng-instal modul pytest dan coverage 
```
(flask-practice) C:\Users\Riska\flask-tutorial>pip install pytest coverage
```

#### 1. Setup and Fixtures
Menguji *code* pada file di *directory* test. 

test/data.sql
```sql
INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');
```

test/conftest.py
```python
import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```

#### 2. Factory
test/test_factory.py
```python
from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```

#### 3. Database
test/test_db.py
```python
import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
```

Menambahkan *command* init-db kedalam file **test_db.py**.
test/test_db.py
```python
def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
```

#### 4. Authentication
tests/conftest.py
```python
class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
```

tests/test_auth.py
```python
import pytest
from flask import g, session
from flaskr.db import get_db


def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'a'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data
```

tests/test_auth.py
```python
def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data
```

tests/test_auth.py
```python
def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session
```

#### 5. Blog
tests/test_blog.py - index
```python
import pytest
from flaskr.db import get_db


def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data
```

tests/test_blog.py - update or delete
```python
@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/delete',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login"


def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403
    # current user doesn't see edit link
    assert b'href="/1/update"' not in client.get('/').data


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/delete',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404
```

tests/test_blog.py - create
```python
def test_create(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'body': ''})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2


def test_update(client, auth, app):
    auth.login()
    assert client.get('/1/update').status_code == 200
    client.post('/1/update', data={'title': 'updated', 'body': ''})

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post['title'] == 'updated'


@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
))
def test_create_update_validate(client, auth, path):
    auth.login()
    response = client.post(path, data={'title': '', 'body': ''})
    assert b'Title is required.' in response.data
```

tests/test_blog.py - delete
```python
def test_delete(client, auth, app):
    auth.login()
    response = client.post('/1/delete')
    assert response.headers["Location"] == "/"

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None
```

#### 6. Running the Tests
setup.cfg
```
[tool:pytest]
testpaths = tests

[coverage:run]
branch = True
source =
    flaskr
```

pytest
```
(flask-practice) C:\Users\Riska\flask-tutorial>pytest
```

coverage
```
(flask-practice) C:\Users\Riska\flask-tutorial>covarage run -m pytest
```

coverage report
```
(flask-practice) C:\Users\Riska\flask-tutorial>covarage report
```

coverage html
```
(flask-practice) C:\Users\Riska\flask-tutorial>covarage html
```

### j. Deploy to Production
#### 1. Build and Install 
Melakukan deploy aplikasi menggunakan cara pendistribusian file yang lain dengan standar untuk Python dalam bentuk wheel dengan extensi .whl.

```
(flask-practice) C:\Users\Riska\flask-tutorial>pip install wheel
```

```
(flask-practice) C:\Users\Riska\flask-tutorial>python setup.py bdist_wheel
```

```
(flask-practice) C:\Users\Riska\flask-tutorial>python install flaskr-1.0.0-py3-none-any.whl
```

menjalankan *command* init-db :
```
(flask-practice) C:\Users\Riska\flask-tutorial>set FLASK_APP=flaskr
(flask-practice) C:\Users\Riska\flask-tutorial>flask init-db
```

#### 2. Configure the Secret Key
```
(flask-practice) C:\Users\Riska\flask-tutorial>python -c 'import secrets; print(secrets.token_hex())'

'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```

#### 3. Run with a Production Server
```
(flask-practice) C:\Users\Riska\flask-tutorial>pip install waitress
```

```
(flask-practice) C:\Users\Riska\flask-tutorial>waitress-serve --call 'flaskr:create_app'

Serving on http://0.0.0.0:8080
```

