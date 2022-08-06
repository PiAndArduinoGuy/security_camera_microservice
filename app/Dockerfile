FROM  piandarduinoguy/raspbian-bullseye-python3-pip:20220427
WORKDIR /security_camera_microservice
COPY src/requirements.txt .
RUN pip3 install -r requirements.txt
COPY src .
RUN mkdir "/security_camera_microservice/logs" \
    && ln -sf /dev/stdout /security_camera_microservice/logs/security-camera-micro-service.log
RUN raspi-config nonint do_camera 0 # enable camera interface
CMD ["python3", "./main.py"]