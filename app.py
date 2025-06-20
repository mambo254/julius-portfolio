from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os
import json

app = Flask(__name__)

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'muendomambo@gmail.com'
app.config['MAIL_PASSWORD'] = 'iinruhvhfhmcufln'  # App Password
mail = Mail(app)

# Home Route
@app.route('/')
def home():
    with open(os.path.join('data', 'projects.json')) as f:
        projects = json.load(f)
    return render_template('index.html', projects=projects)

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Projects Route (optional separate route)
@app.route('/projects')
def projects():
    with open(os.path.join('data', 'projects.json')) as f:
        projects = json.load(f)
    return render_template('index.html', projects=projects)

# Blog Overview Page
@app.route('/blog')
def blog():
    with open(os.path.join('data', 'blog.json')) as f:
        blog_posts = json.load(f)
    return render_template('blog.html', blog_posts=blog_posts)

# Blog Post Detail Page
@app.route('/blog/<slug>')
def blog_post(slug):
    with open(os.path.join('data', 'blog.json')) as f:
        blog_posts = json.load(f)
    post = next((p for p in blog_posts if p['slug'] == slug), None)
    if post:
        return render_template('blog_post.html', post=post)
    else:
        return "Post not found", 404

# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject=f"New Contact from {name}",
                      sender=email,
                      recipients=['muendomambo@gmail.com'],
                      body=message)
        try:
            mail.send(msg)
            return render_template('contact.html', success=True)
        except Exception as e:
            print("Email sending error:", e)
            return render_template('contact.html', error=True)
    return render_template('contact.html')

# Run the App
if __name__ == '__main__':
    print("🚀 Starting Flask server...")
    app.run(debug=True)
