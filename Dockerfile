FROM python:3.8
ADD requirements.txt /patchy-bot/
RUN pip install -r /patchy-bot/requirements.txt
COPY . /patchy-bot/

CMD [ "python", "./patchy-bot/patchy.py" ]