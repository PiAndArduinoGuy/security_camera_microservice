FROM raspbian/stretch
RUN apt update
# TODO: install python3.8 as the syntax lekker: string = 'kwaai' is invalid for python 3.5 installed by the below call
RUN apt install python3 -y
RUN apt install python3-pip -y
WORKDIR /security_camera_microservice
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src/ .
CMD ["python3", "./main.py"]