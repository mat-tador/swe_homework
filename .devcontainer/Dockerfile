FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /workspace


RUN apt-get update && apt-get install -y \
    python3 python3-pip python-is-python3 \
    tar bzip2 g++ clang cmake make ninja-build wget git \
    libsqlite3-dev libgtk-3-dev libboost-all-dev \
    neovim \
    iproute2 net-tools iputils-ping \
    && rm -rf /var/lib/apt/lists/*


RUN pip3 install numpy matplotlib pandas pytest pytest-cov --break-system-packages


RUN echo 'PS1="\e[01;32m\u@\h\e[m:\e[01;34m\w\e[m\$ "' >> /root/.bashrc



CMD ["/bin/bash"]