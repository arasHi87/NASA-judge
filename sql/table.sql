CREATE TYPE mood AS ENUM ('pending', 'evaluating', 'done');

CREATE TABLE IF NOT EXISTS results(
    rid SERIAL PRIMARY KEY,
    uid VARCHAR NOT NULL,
    pid INTEGER NOT NULL,
    score INTEGER NOT NULL,
    status mood DEFAULT 'pending' NOT NULL
);

CREATE TABLE IF NOT EXISTS users(
    uid VARCHAR PRIMARY KEY,
    token VARCHAR NOT NULL
);