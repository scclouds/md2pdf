FROM python:3.8
LABEL Maintainer="SC Clouds <contato@scclouds.com.br> (@scclouds)"

RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN tar xvf wkhtmltox*.tar.xz
RUN mv wkhtmltox/bin/wkhtmlto* /usr/bin

RUN apt-get update -y
RUN apt-get install -y \
    openssl \
    build-essential \
    libssl-dev \
    libxrender-dev \
    git-core \
    libx11-dev \
    libxext-dev \
    libfontconfig1-dev \
    libfreetype6-dev \
    fontconfig

WORKDIR /usr/bin/

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY md2pdf_converter.py ./
COPY docker-entrypoint.sh ./

ENTRYPOINT ["docker-entrypoint.sh"]