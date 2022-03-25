from string import digits, ascii_letters
from datetime import datetime
from random import choices
from URL_Shortening_Service import db


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def random_token(size = 6):
    """
    Generates a random string of 6 chars , use size argument 
    to change the size of token.
    Returns a valid token of desired size , 
    *default is 6 chars
    """
    BASE_LIST = digits + ascii_letters
    token = ''.join(choices(BASE_LIST, k = size))
    return token


class Link(db.Model):
    """docstring for Link"""
    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.String(300))
    shorten_url = db.Column(db.String(16), unique = True)
    created_time = db.Column(db.DateTime, default = datetime.now)
    visits = db.Column(db.Integer, default = 0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shorten_url += self.generate_shorter_url()

    def generate_shorter_url(self):
        """
        Walk up with such naive algorithm, wait till the end ...
        """
        chr_and_digit = digits + ascii_letters
        shorten_url = ''.join(choices(chr_and_digit, k = 3))
        link = self.query.filter_by(shorten_url = shorten_url).first()
        if link:
            self.generate_shorter_url()
        return shorten_url
