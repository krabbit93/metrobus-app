FROM python:3.7.8-slim

WORKDIR /usr/src/app
RUN apt-get update && apt-get install --no-install-recommends -y cron

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN touch /usr/src/environ
RUN touch /var/log/microbus_cron.log

RUN echo 'SHELL=/bin/bash' > /etc/cron.d/microbus_cron
RUN echo '* * * * * /usr/src/run_py.sh > /proc/1/fd/1 2>/proc/1/fd/2' >> /etc/cron.d/microbus_cron
RUN echo '#empty line for cron file' >> /etc/cron.d/microbus_cron
RUN chmod 644 /etc/cron.d/microbus_cron

RUN echo "source /usr/src/environ &&" > /usr/src/run_py.sh
RUN echo "$(which python) /usr/src/app/unit_location_sync.py" >> /usr/src/run_py.sh
RUN chmod +x /usr/src/run_py.sh

COPY . .

RUN crontab /etc/cron.d/microbus_cron

CMD env > /usr/src/environ && sed -i -e 's/^/export /' /usr/src/environ && cron -f