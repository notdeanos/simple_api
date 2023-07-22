FROM python:3.8
RUN apt-get update && apt-get install -y net-tools strace iputils-ping
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3002
CMD ["/usr/local/bin/python", "index.py"]

