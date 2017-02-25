#!/bin/bash
set -e
export DJANGO_DIR={{ django_dir }}
export PROJECT_DIR={{ project_dir }}
export LOGFILE=$PROJECT_DIR/logs/gunicorn.log
export LOGDIR=$(dirname $LOGFILE)
export NUM_WORKERS=3

cd {{ project_dir }}
source $PROJECT_DIR/venv/bin/activate
export DATABASE_URL='postgres://{{ db_user }}:{{ db_password }}@localhost/{{ db_name }}'
export PYTHONPATH=$DJANGO_DIR:$PYTHONPATH

test -d $LOGDIR || mkdir -p $LOGDIR
exec $PROJECT_DIR/venv/bin/gunicorn weather_station.wsgi:application -w $NUM_WORKERS \
  --log-level=info --log-file=$LOGFILE -b 0.0.0.0:9000 2>>$LOGFILE
