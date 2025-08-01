# Base image
FROM ubuntu:22.04

# Set non-interactive frontend for apt
ENV DEBIAN_FRONTEND=noninteractive

# Update package index
RUN apt-get update

# Core tools
RUN apt-get install -y build-essential
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install -y man
RUN apt-get install -y sudo
RUN apt-get install -y vim
RUN apt-get install -y wget
RUN apt-get install -y tree

# Locale configuration
RUN apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Go (for Hugo development)
RUN apt-get install -y golang-go

# Node.js (latest LTS) and npm (for commitlint, husky, and codex)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

# Update npm to latest version
RUN npm install -g npm@latest

# Hugo installation (extended, auto-detect architecture)
RUN ARCH=$(dpkg --print-architecture) && \
    wget https://github.com/gohugoio/hugo/releases/download/v0.146.0/hugo_extended_0.146.0_linux-${ARCH}.deb && \
    dpkg -i hugo_extended_0.146.0_linux-${ARCH}.deb && \
    rm hugo_extended_0.146.0_linux-${ARCH}.deb

# Clean up APT cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Default command
CMD [ "bash" ]
