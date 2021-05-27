from bs4 import BeautifulSoup
from bs4.builder import TreeBuilder

class Parser:

    html = ""

    def __init__(self, html):
        self.html = html

    def get_content(self):
        soap = BeautifulSoup(self.html, 'html.parser')
        message_block = soap.find('div', class_='VUU41')
        if message_block != None:
            messages_text = message_block.find_all('div', class_='YBx95')

            for i in messages_text:
                print('message', i.get_text(strip=True))
