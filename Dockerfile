FROM ubuntu:rolling
COPY ./ENTRYPOINT.py /ENTRYPOINT.py
COPY ./DATABASE.jsonc /DATABASE.jsonc
RUN apt-get update -y && apt-get install -y apt-utils sudo python3.11 python3-pip && python3.11 -m pip install --user pipenv && sudo apt-get full-upgrade -y && sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1
ENTRYPOINT [ "/bin/bash", "-c", "FULL_QUOTE=$(python3.11 /ENTRYPOINT.py $1) && echo FULL_QUOTE=$FULL_QUOTE >> $GITHUB_OUTPUT" ]