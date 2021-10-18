-- migrate:up
---- https://github.com/amacneil/dbmate#clickhouse ----
CREATE DATABASE IF NOT EXISTS search_log

-- migrate:down
DROP DATABASE IF EXISTS search_log
