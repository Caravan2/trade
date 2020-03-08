import requests, re
from flask import Flask, request
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tricoin.info@gmail.com'
app.config['MAIL_PASSWORD'] = 'xulkjfwgbsbvxjtv'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/", methods=["POST"])
def index():
    req = request.get_json(force=True)
    Person = req["queryResult"]["queryText"]

    url = f'http://export.arxiv.org/api/query?search_query=all:{Person}&start=0&max_results=1'
    data = requests.get(url).text
    summary = data.split("summary>")
    summary = summary[1][:-2]
    title = data.split("title>")
    title = title[2][:-2]
    # title = data.split("<title")
    # title = re.search('<title>(.+?)</title>', str(data))
    # p = re.search('<entry>(.+?)</entry>', str(data))
    raw = data.split()
    links = []
    for raw in raw:
        if 'href="http://arxiv.org' in raw:
            raw = raw.split('"')
            links.append(raw[1])
    web = links[1]
    pdf = links[2]
    # return title + "================" + summary + web + pdf
    return {'fulfillmentText': f"{title} \n\n {summary} \n\n web: {web} \n pdf: {pdf}"}

@app.route("/ai")
def ai():
    url = 'http://export.arxiv.org/api/query?search_query=all:ai&start=0&max_results=1'
    data = requests.get(url).text
    summary = data.split("summary>")
    summary = summary[1][:-2]
    title = data.split("title>")
    title = title[2][:-2]
    # title = data.split("<title")
    # title = re.search('<title>(.+?)</title>', str(data))
    # p = re.search('<entry>(.+?)</entry>', str(data))
    raw = data.split()
    links = []
    for raw in raw:
        if 'href="http://arxiv.org' in raw:
            raw = raw.split('"')
            links.append(raw[1])
    web = links[1]
    pdf = links[2]
    # return title + "================" + summary + web + pdf

    msg = Message('Artificial Intelligence', sender = "tricoin.info@gmaigmail.com", recipients = ['mirianchkhvimiani@gmail.com'])
    msg.body = f"{title} \n\n {summary} \n\n {web} \n {pdf}"
    mail.send(msg)

@app.route("/ml")
def ml():
    url = 'http://export.arxiv.org/api/query?search_query=all:ml&start=0&max_results=1'
    data = requests.get(url).text
    summary = data.split("summary>")
    summary = summary[1][:-2]
    title = data.split("title>")
    title = title[2][:-2]
    # title = data.split("<title")
    # title = re.search('<title>(.+?)</title>', str(data))
    # p = re.search('<entry>(.+?)</entry>', str(data))
    raw = data.split()
    links = []
    for raw in raw:
        if 'href="http://arxiv.org' in raw:
            raw = raw.split('"')
            links.append(raw[1])
    web = links[1]
    pdf = links[2]
    # return title + "================" + summary + web + pdf

    msg = Message('Machine Learning', sender = "tricoin.info@gmaigmail.com", recipients = ['mirianchkhvimiani@gmail.com'])
    msg.body = f"{title} \n\n {summary} \n\n {web} \n {pdf}"
    mail.send(msg)

    return title + "================" + summary + web + pdf


@app.route("/dl")
def dl():
    url = 'http://export.arxiv.org/api/query?search_query=all:deep learning&start=0&max_results=1'
    data = requests.get(url).text
    summary = data.split("summary>")
    summary = summary[1][:-2]
    title = data.split("title>")
    title = title[2][:-2]
    # title = data.split("<title")
    # title = re.search('<title>(.+?)</title>', str(data))
    # p = re.search('<entry>(.+?)</entry>', str(data))
    raw = data.split()
    links = []
    for raw in raw:
        if 'href="http://arxiv.org' in raw:
            raw = raw.split('"')
            links.append(raw[1])
    web = links[1]
    pdf = links[2]
    # return title + "================" + summary + web + pdf

    msg = Message('Deep Learning', sender = "tricoin.info@gmaigmail.com", recipients = ['mirianchkhvimiani@gmail.com'])
    msg.body = f"{title} \n\n {summary} \n\n {web} \n {pdf}"
    mail.send(msg)
if __name__ == '__main__':
    app.run(debug = True)
