FROM navikey/raspbian-bullseye:2022-05-08
RUN apt update -y
RUN apt install -y python3 python3-pip
WORKDIR /security_camera_microservice
COPY src/requirements.txt .
RUN pip3 install -r requirements.txt
COPY src .
RUN mkdir "/security_camera_microservice/logs" \
    && ln -sf /dev/stdout /security_camera_microservice/logs/security-camera-micro-service.log
CMD ["python3", "./main.py"]