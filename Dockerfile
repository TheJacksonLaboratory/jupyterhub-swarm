FROM python:3.6
RUN pip3 install \
    jupyterhub==0.7.2 \
    'notebook>=5.0,<=6.0'


# create a user, since we don't want to run as root
RUN useradd -m ubuntu
ENV HOME=/home/ubuntu
WORKDIR $HOME
USER ubuntu

CMD ["jupyterhub-singleuser"]
