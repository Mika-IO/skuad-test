FROM python:3

WORKDIR /usr/src/app

# Colocando os arquivos python no container
COPY requirements.txt ./
COPY src/script1.py ./
COPY src/script2.py ./
COPY src/api.py ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./api.py" ]