
--
-- Database schema
--

CREATE DATABASE default IF NOT EXISTS;

CREATE TABLE default.schema_migrations
(
    `version` String,
    `ts` DateTime DEFAULT now(),
    `applied` UInt8 DEFAULT 1
)
ENGINE = ReplacingMergeTree(ts)
PRIMARY KEY version
ORDER BY version
SETTINGS index_granularity = 8192;

CREATE TABLE default.search_log
(
    `timestamp` DateTime('Europe/Moscow'),
    `query` String,
    `action` String,
    `tile_id` UInt8,
    `user_agent` String
)
ENGINE = Log;


--
-- Dbmate schema migrations
--

INSERT INTO schema_migrations (version) VALUES
    ('20211014151723'),
    ('20211014151732');
