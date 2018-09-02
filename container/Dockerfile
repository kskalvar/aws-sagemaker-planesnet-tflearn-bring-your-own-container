# Build an image that can do training and inference in SageMaker
# This is a Python 2 image that uses the tflearn, nginx, gunicorn, flask stack
# for serving inferences in a stable way.

FROM ubuntu:16.04
RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget vim \
         python \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*
    
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && \
    pip install numpy==1.14.0 scipy==1.1.0 flask==1.0.2 gevent==1.3.6 gunicorn==19.9.0 tensorflow==1.5.0 tflearn==0.3.2 h5py==2.8.0 && \
        (cd /usr/local/lib/python2.7/dist-packages/scipy/.libs; rm *; ln ../../numpy/.libs/* .) && \
        rm -rf /root/.cache

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY decision_trees /opt/program
WORKDIR /opt/program
