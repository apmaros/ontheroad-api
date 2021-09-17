FROM python:3.8-slim

ARG APP_VERSION
ENV APP_VERSION=$APP_VERSION

# setup working directory for container
WORKDIR /usr/src/app
# copy project to the image
COPY . .

# install psql drivers
RUN apt-get update \
  && apt-get install gcc -y \
  && apt-get clean

# install dependencies
RUN pip install --no-cache-dir -r requirements/prod.txt

# expose API port
EXPOSE 4000

CMD [ "/bin/bash", "/usr/src/app/bin/run" ]
