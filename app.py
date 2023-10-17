# app.py



from flask import Flask, render_template, request, redirect, url_for



app = Flask(_name_)


# Dummy data for articles (You'd use a database in a real application)

articles = [

    {'id': 1, 'title': 'Article 1', 'content': 'This is the first article.'},

    {'id': 2, 'title': 'Article 2', 'content': 'This is the second article.'},

    # Add more articles as needed

]


@app.route('/')

def index():

    return render_template('index.html', articles=articles)



@app.route('/article/<int:id>')

def view_article(id):

    article = next((article for article in articles if article['id'] == id), None)

    return render_template('view_article.html', article=article)



@app.route('/add_article', methods=['GET', 'POST'])

def add_article():

    if request.method == 'POST':

        title = request.form['title']

        content = request.form['content']

        new_article = {'id': len(articles) + 1, 'title': title, 'content': content}
                  articles.append(new_article)
        return redirect(url_for('index'))

    return render_template('add_article.html')



@app.route('/edit_article/<int:id>', methods=['GET', 'POST'])

def edit_article(id):

    article = next((article for article in articles if article['id'] == id), None)

    if request.method == 'POST':

        article['title'] = request.form['title']

        article['content'] = request.form['content']

        return redirect(url_for('index'))

    return render_template('edit_article.html', article=article)



@app.route('/delete_article/<int:id>')

def delete_article(id):

    global articles

    articles = [article for article in articles if article['id'] != id]

    return redirect(url_for('index'))



if _name_ == '_main_':

    app.run(debug=True)



