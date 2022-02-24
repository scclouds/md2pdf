FROM python:3.8
LABEL Maintainer="SC Clouds <contato@scclouds.com.br> (@scclouds)"

RUN apt-get update -y
RUN apt-get install wkhtmltopdf -y

WORKDIR /usr/bin/

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY md2pdf_converter.py ./
COPY docker-entrypoint.sh ./

ENTRYPOINT ["docker-entrypoint.sh"]