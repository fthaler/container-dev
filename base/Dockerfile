FROM ubuntu:latest
LABEL maintainer="Felix Thaler <felix.thaler@nummi.ch>"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -qq && \
    apt-get install -qq -y \
        build-essential \
        clang-format \
        cmake \
        gdb \
        curl \
        git \
        language-pack-en-base \
        neovim \
        python3 \
        python3-pip \
        python3-pynvim \
        software-properties-common \
        tmux \
        wget && \
    rm -rf /var/list/apt/lists/*

COPY rcs /checkouts/rcs
RUN ln -s /checkouts/rcs/tmux.conf $HOME/.tmux.conf && \
    mkdir -p $HOME/.config/nvim/ && \
    ln -s /checkouts/rcs/vimrc $HOME/.config/nvim/init.vim
RUN echo "source /checkouts/rcs/bashrc" >> $HOME/.bashrc
RUN nvim --headless +PlugInstall +qa
