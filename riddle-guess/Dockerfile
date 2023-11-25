FROM python:3.10
WORKDIR /home/riddle-server/
COPY . .
RUN apt-get update && \
apt-get install -y python3-pip && \  
python3 -m pip install redis[hiredis] &&  \
python3 -m pip install flask && \
python3 -m pip install flask[async]
EXPOSE 5000
CMD ["python3", "riddle-guess.py"]

