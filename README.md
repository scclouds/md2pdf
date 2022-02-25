# md2pdf

[![Build Status](https://github.com/scclouds/md2pdf/workflows/ci/badge.svg)](https://github.com/scclouds/md2pdf/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/scclouds/md2pdf.svg)](https://store.docker.com/community/images/scclouds/md2pdf)
[![license](https://img.shields.io/github/license/scclouds/md2pdf.svg)](https://github.com/scclouds/md2pdf/blob/master/LICENSE)

Simple python script to convert MD to PDF.

# How to use

```sh
docker run -v <PATH_TO_DIR_WITH_MD_FILES>:/mnt/temp scclouds/md2pdf:latest <OUTPUT_NAME>.pdf
```
