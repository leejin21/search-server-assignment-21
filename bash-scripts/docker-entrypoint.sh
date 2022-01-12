#!/bin/sh

chmod u+x /app/bash-scripts/wait-for-postgres.sh
/bin/bash /app/bash-scripts/wait-for-postgres.sh

flask db init
flask db stamp head
flask db migrate
flask db upgrade
python3 -m flask run --host=0.0.0.0