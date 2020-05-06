import os
import requests
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    url = "http://unkno.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def piggy_words(fact):

    url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    payload = {'input_text': fact}
    r = requests.post(url, payload, allow_redirects=False)
    location = r.headers['Location']
    a_href = f'<a href={location}>{location}</a>'
    return a_href


@app.route('/')
def home():

    fact = get_fact()
    return piggy_words(fact)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
