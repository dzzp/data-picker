#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --dbname "$POSTGRES_DB" <<-EOSQL
    ALTER ROLE $POSTGRES_USER SET client_encoding TO 'utf8';
    ALTER ROLE $POSTGRES_USER SET default_transaction_isolation TO 'read committed';
EOSQL
