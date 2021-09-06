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
RUN python -m pip install pymongo[srv]

# copy project
COPY . .
CMD ["uvicorn", "api.main:app", "--host",  "0.0.0.0", "--port", "8000", "--reload"]