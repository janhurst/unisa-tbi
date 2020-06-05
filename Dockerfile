FROM python

# note - /home is overwritten in Azure App Service when persistent storage is used
WORKDIR /src

# install the requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy Python data package source files
COPY ./src/data/ ./data/
COPY ./src/ui ./ui/
COPY ./src/app.py ./app.py

# configure environment
ENV NEPTUNE_PROJECT="unisa-tbi/unisa-tbi"
ENV PYTHONPATH="/src"

# set the startup command
EXPOSE 80
CMD waitress-serve --host 0.0.0.0 --port 80 app:app
