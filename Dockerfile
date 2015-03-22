FROM ubuntu:14.04
MAINTAINER vicent@tangotree.io

RUN apt-get update && apt-get install -y supervisor python-dev curl

# Pip could not be installed using apt-get. It retrieved an old version that crashed trying to install nose and mock.
# This new version runs smoothly
RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python2.7

ADD . /code

WORKDIR /code
RUN pip install -r ./requirements.txt

CMD ["/usr/bin/supervisord"]
