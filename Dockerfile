FROM python:3.8
LABEL Maintainer="SC Clouds <contato@scclouds.com.br> (@scclouds)"

RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN tar xvf wkhtmltox*.tar.xz
RUN mv wkhtmltox/bin/wkhtmlto* /usr/bin

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32
RUN echo "deb http://security.ubuntu.com/ubuntu bionic-security main" >> /etc/apt/sources.list

RUN apt-get update -y
RUN apt-cache policy libssl1.0-dev
RUN apt-get install -y \
    openssl \
    build-essential \
    libssl1.0-dev \
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

ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY md2pdf_converter.py ./
COPY docker-entrypoint.sh ./
COPY conf.yaml ./
COPY toc.xsl ./

ENTRYPOINT ["docker-entrypoint.sh"]