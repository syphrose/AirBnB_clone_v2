Web - Frameworks
A software framework that is designed to support the development of web applications including web services, web resources and web APIs.

Types of Frameworks:
a) Server-side (backend)
b) Web frameworks
c) User-side (frontend)

Server-side (backend)
Their architecture and rules permit you to create simple pages, landings and forms of different kinds. You'll need a wider range of functionality to create a web application with a well-developed interface.

These frameworks handle HTTP requests, database control and management, URL mapping, etc.They can as well improve security and form the output data- simplifying the development process.

Some of the top server-side frameworks are;

a) NET (C#)
b) Django (Python)
c) Ruby on Rails (Ruby)
d) Express (JavaScript/Node.JS)
e) Symfony (PHP)

They are a piece of software that offers a way to create and run web applications.


Client-side Frameworks
They function inside the browser thus you can enhance and implement new user interfaces.

A number of animated features can be created with frontend and single page applications.

The Frameworks include;
1. Angular
2. Ember.JS
3. Vue.JS
4. React.JS

Web application framework- Architecture

Most of the web frameworks depend on the MVC (Model-View-Controller) architecture. The reason why this pattern is preferred lies in its rational design that separates the app logic from the interface and forms the three essential parts that are represented in the architecture’s name — MVC (Model-View-Controller).

Model
The Model comprises of all the data, business logic layers, its guidelines and functions. The Model, upon getting user input data from the Controller, tells the way an updated interface should be displayed directly to the View.

View
The View is for the graphical representation of the data like graph or charts etc. It is the apps’ front-end. The View gets the user input and communicates the same to the Controller for examination and then update and reconstructs itself according to the Model’s instructions, or the Controller’s in case the modification requirement is minimum.

Controller
The Controller translates the input data into the scope of commands of the previous ones. It is the midway between the Model and the View. It gets the user input from the View; after processing it, the Controller notifies the Model (or View) of the changes required.

A Minimal Application
A minimal Flask application looks something like this:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
So what did that code do?

First we imported the Flask class. An instance of this class will be our WSGI application.

Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

We then use the route() decorator to tell Flask what URL should trigger our function.

The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

Save it as hello.py or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.

To run the application, use the flask command or python -m flask. You need to tell the Flask where your application is with the --app option.

$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

Externally Visible Server

If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

$ flask run --host=0.0.0.0
This tells your operating system to listen on all public IPs.

Debug Mode

The flask run command can do more than just start the development server. By enabling debug mode, the server will automatically reload if code changes, and will show an interactive debugger in the browser if an error occurs during a request.

To enable debug mode, use the --debug option.

$ flask --app hello run --debug
 * Serving Flask app 'hello'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn

HTML Escaping

When returning HTML (the default response type in Flask), any user-provided values rendered in the output must be escaped to protect from injection attacks. HTML templates rendered with Jinja, introduced later, will do this automatically.

Routing

Modern web applications use meaningful URLs to help users. Users are more likely to like a page and come back if the page uses a meaningful URL they can remember and use to directly visit a page.

