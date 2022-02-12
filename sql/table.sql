CREATE TYPE mood AS ENUM ('pending', 'evaluating', 'done');

CREATE TABLE IF NOT EXISTS results(
    rid INTEGER PRIMARY KEY,
    uid INTEGER NOT NULL,
    pid INTEGER NOT NULL,
    score INTEGER NOT NULL,
    status mood DEFAULT 'pending' NOT NULL
);

CREATE TABLE IF NOT EXISTS users(
    uid VARCHAR PRIMARY KEY,
    token VARCHAR NOT NULL
);