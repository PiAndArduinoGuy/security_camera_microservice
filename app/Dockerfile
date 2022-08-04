FROM navikey/raspbian-bullseye:2022-05-08
RUN apt update -y
RUN apt install -y python3 python3-pip
WORKDIR /security_camera_microservice
COPY ../requirements.txt .
RUN pip3 install -r requirements.txt
COPY src .
CMD ["python3", "./main.py", "--rabbitmq_host_ip", "192.168.3.147", "--security_config_queue_name", "updated.security.config", "--security_config_exchange_name", "fanout_exchange", "--logging_file_directory" ,"./output/security_camera_microservice.log", "--security_micro_service_context_path", "/security", "--security_micro_service_host_ip","192.168.3.147", "--security_micro_service_host_port", "8082", "--security_camera_microservice_capture_directory", "./output"]