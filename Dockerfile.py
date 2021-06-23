FROM nvidia/cuda:9.2-cudnn7-devel-ubuntu16.04 

ENV DEBIAN_FRONTEND=noninteractive 

RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    rm -rf /var/lib/apt/lists/* \
           /etc/apt/sources.list.d/cuda.list \
           /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    wget \
    openssh-client \
    openssh-server \
    autossh \
    git \
    libopencv-dev \
    time \
    vim \
    unzip \
    tmux 

# install python2
RUN apt-get install -y --no-install-recommends python2.7 python-dev && \
    wget https://bootstrap.pypa.io/pip/2.7/get-pip.py && python get-pip.py && \
    mkdir ~/.pip && echo "[global]" > ~/.pip/pip.conf && \
	echo "index-url=https://pypi.tuna.tsinghua.edu.cn/simple" >> ~/.pip/pip.conf && \
	echo "format = columns" >> ~/.pip/pip.conf

# install python3
# RUN apt-get install -y --no-install-recommends software-properties-common && \
#     add-apt-repository ppa:deadsnakes/ppa && \
#     apt-get update && \
#     apt-get install -y --no-install-recommends python3.7 python3.7-dev && \
#     rm /usr/bin/python && ln -s /usr/bin/python3.7 /usr/bin/python && \
#     wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && \
#     mkdir ~/.pip && echo "[global]" > ~/.pip/pip.conf && \
#     echo "index-url=https://pypi.mirrors.ustc.edu.cn/simple/" >> ~/.pip/pip.conf  &&\                                                                            
#     echo "format = columns" >> ~/.pip/pip.conf

# install java
# RUN wget  --no-check-certificate --no-cookies --header "Cookie:oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz && \
#     tar -zxvf jdk-8u131-linux-x64.tar.gz && \
#     mv jdk1.8.0_131 jdk1.8 && \
#     mv jdk1.8 /usr/local 

# ENV JAVA_HOME=/usr/local/jdk1.8
# ENV JRE_HOME=${JAVA_HOME}/jre
# ENV CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib:$CLASSPATH
# ENV JAVA_PATH=${JAVA_HOME}/bin:${JRE_HOME}/bin
# ENV PATH=$PATH:${JAVA_PATH}

COPY torch-0.4.1-cp27-cp27mu-manylinux1_x86_64.whl  /tmp

RUN pip install /tmp/torch-0.4.1-cp27-cp27mu-manylinux1_x86_64.whl\
                torchvision==0.2.2\
                numpy\
                python-dateutil\
                easydict\
                pandas\
                torchfile\
                nltk \
                scikit-image \
                Pillow

RUN rm -rf /tmp/torch-0.4.1-cp27-cp27mu-manylinux1_x86_64.whl
# ------------------------------------------------------------------
Run ldconfig && \
  apt-get -y clean && \
  apt-get -y autoremove && \
  rm -rf /var/lib/apt/lists/* /tmp/* ~/*
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN echo 'Asia/Shanghai' >/etc/timezone
WORKDIR /

#RUN echo "root:ustc" | chpasswd
#RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
