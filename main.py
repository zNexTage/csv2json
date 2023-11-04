from fastapi.responses import FileResponse, Response
from fastapi import FastAPI, UploadFile

import csv
import codecs
import json

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    ''' Página inicial que será utilizada para controlar o Rover. '''
    return FileResponse('static/index.html')

@app.post("/convert")
async def convert(upload_file:UploadFile):
    #In Python3, csv.reader expects, that passed iterable returns strings, not bytes. Here is one more solution to this problem, that uses codecs module:
    #Ref: https://stackoverflow.com/questions/8515053/csv-error-iterator-should-return-strings-not-bytes
    dict_csv = csv.DictReader(codecs.iterdecode(upload_file.file, encoding="utf-8"))

    json_itens = []

    for row in dict_csv:
        json_itens.append(row)

    headers = {
        'Content-Disposition': 'attachment; filename="teste.json"',
        'Content-Type': 'charset=utf-8'
    }

    json_content = json.dumps(json_itens, ensure_ascii=False)

    return Response(json_content, headers=headers, media_type="application/octet-stream")
