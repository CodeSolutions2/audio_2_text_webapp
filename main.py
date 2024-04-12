from openai import OpenAI
from pyweb import pydom
from pyodide.http import open_url
from pyscript import display
from js import console

title = "OpenAI (and basic DOM manipulation)"
page_message = "This example loads a remote mp3 file into a OpenAI, and displays result."

# download_url of the file_object
url = "https://raw.githubusercontent.com/CodeSolutions2/audio_2_text_webapp/main/2024_03_13_09_58_13_test1.mp3"

pydom["title#header-title"].html = title
pydom["a#page-title"].html = title
pydom["div#page-message"].html = page_message
pydom["input#txt-url"][0].value = url

def log(message):
    # log to pandas dev console
    # print(message)
    # log to JS console
    console.log(message)

def loadFromURL(event):
    pydom["div#python-output-inner"].html = ""
    url = pydom["input#txt-url"][0].value

    log(f"Trying to login")
    client = OpenAI(api_key = OPENAI_API_KEY)

    log(f"Trying to fetch mp3 from {url}")
    audio_file = open(open_url(url), "rb")
    transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

    pydom["div#python-output"].style["display"] = "block"

    display(transcription.text, target="python-output-inner", append="False")
