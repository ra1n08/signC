from cypher import createParameter, signC, un_signC
from flask import Flask
# import sys
# import functools
# import threading
# from colorama import Fore, Back, Style
# import asyncio

app = Flask(__name__)

@app.route("/createParameter")
def main():
    return "hello world!"


if __name__ == "__main__":
    app.run()