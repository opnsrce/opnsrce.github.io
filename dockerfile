FROM ruby:3.0

# Set `DEVCONTAINER` environment variable to help with orientation
ENV DEVCONTAINER=true

# Create the directory all the code from your machine will be copied to
WORKDIR /workspace

COPY . /workspace/

# Install basic development tools
RUN apt update && apt install -y less man-db sudo

# Install vim
RUN apt install -y vim

# Install project gems
RUN bundle install

# Install Jekyll
RUN gem install jekyll

