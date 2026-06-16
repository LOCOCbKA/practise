#!/bin/bash
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="./backups"
mkdir -p $BACKUP_DIR
docker exec -t app_db pg_dump -U testuser testdb > $BACKUP_DIR/db_backup_$TIMESTAMP.sql
echo "Backup created: $BACKUP_DIR/db_backup_$TIMESTAMP.sql"
