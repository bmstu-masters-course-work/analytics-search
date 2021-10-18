-- migrate:up
CREATE TABLE IF NOT EXISTS search_log
(
    `timestamp`  DateTime('Europe/Moscow') NOT NULL,
    `query`      String NOT NULL,
    `action`     String NOT NULL,
    `tile_id`    UInt8 NOT NULL,
    `user_agent` String NOT NULL
) ENGINE = Log

-- migrate:down
DROP TABLE IF EXISTS search_log
