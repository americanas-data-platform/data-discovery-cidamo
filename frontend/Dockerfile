# pull official base image
FROM python:3.8

# set work directory
WORKDIR /usr/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY requirements.txt ./

# install dependencies
RUN pip install -r /usr/src/requirements.txt
EXPOSE 8501
# copy project
COPY . .
CMD ["streamlit", "run", "main.py", "--server.enableWebsocketCompression=false"]