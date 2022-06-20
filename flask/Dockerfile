# Base image
FROM python:3.9-slim
# Copy contents
COPY . /infra
# Change work directory
WORKDIR /infra/flask
# Install the requirements
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
RUN pip install -r requirements.txt
# Start the application
CMD [ "python3", "-u", "app.py" ]
