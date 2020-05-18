FROM python

WORKDIR /home

# copy UI files
COPY ui/ ./

# copy Python data package source files
COPY ./src/data/ ./data/
COPY ./src/ui ./ui/

# install the requirements
RUN pip install -r requirements.txt

# configure environment
ENV NEPTUNE_PROJECT="unisa-tbi/unisa-tbi"

# set the startup command
EXPOSE 80
CMD waitress-serve --host=0.0.0.0 --port=80 app:app 