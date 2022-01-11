#!/bin/sh
# wait-for-postgres.sh

set -e
  
shift
  
until PGPASSWORD=$PG_PASSWORD psql -h "$PG_HOST" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
  
>&2 echo "Postgres is up - executing command"