FROM fthaler/container-dev:base
LABEL maintainer="Felix Thaler <felix.thaler@nummi.ch>"

RUN apt-get update -qq && \
    apt-get install -qq -y \
        libboost-all-dev \
        libopenmpi-dev \
        zlib1g-dev && \
    rm -rf /var/list/apt/lists/*

ENV CMAKE_PREFIX_PATH=/usr/local/lib/cmake

#RUN git clone -b release_v1.1 https://github.com/GridTools/gridtools.git && \
    #mkdir -p gridtools/build && \
    #cd gridtools/build && \
    #cmake \
        #-DCMAKE_BUILD_TYPE=Release \
        #-DBUILD_TESTING=OFF \
        #-DGT_ENABLE_BACKEND_X86=ON \
        #-DGT_ENABLE_BACKEND_MC=ON \
        #-DGT_ENABLE_BACKEND_CUDA=OFF \
        #-DGT_ENABLE_BACKEND_NAIVE=OFF \
        #.. && \
    #make -j $(nproc) install && \
    #cd ../.. && \
    #rm -rf gridtools

RUN git clone https://github.com/GridTools/gridtools.git && \
    mkdir -p gridtools/build && \
    cd gridtools/build && \
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_TESTING=OFF \
        .. && \
    make -j $(nproc) install && \
    cd ../.. && \
    rm -rf gridtools

#RUN git clone https://github.com/GridTools/GHEX.git && \
    #mkdir -p GHEX/build && \
    #cd GHEX/build && \
    #cmake \
        #-DCMAKE_BUILD_TYPE=Release \
        #.. && \
    #make -j $(nproc) install && \
    #cd ../.. && \
    #rm -rf GHEX

COPY ycm_extra_conf.py /.ycm_extra_conf.py
