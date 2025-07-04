# 
FROM python:3.9

# 
WORKDIR /code

#upgrade pip

RUN /usr/local/bin/python -m pip install --upgrade pip

#aliyun index

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./application /code/application

# 
CMD ["uvicorn", "application.server.main:app", "--host", "0.0.0.0", "--port", "80"]

