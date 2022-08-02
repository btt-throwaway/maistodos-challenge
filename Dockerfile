FROM python:3.10

WORKDIR /src

# RUN apk add --no-cache --update \
#     python3 python3-dev gcc \
#     gfortran musl-dev \
#     libffi-dev openssl-dev

RUN pip install --upgrade pip

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app/main.py"]