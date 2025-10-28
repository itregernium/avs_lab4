#!/bin/sh

set -e

while ! pg_isready -h $POSTGRES_HOST -p 5432 -U $POSTGRES_USER; do
  sleep 1
done
echo "PostgreSQL started"

flask create-tables

exec "$@"