CREATE TABLE IF NOT EXISTS minions_birthdays (
    "id" SERIAL UNIQUE PRIMARY KEY,
    "name" VARCHAR(50) DEFAULT '',
    date_of_birth DATE NOT NULL,
    age INTEGER DEFAULT 0,
    present VARCHAR(100) DEFAULT '',
    party TIMESTAMPTZ NOT NULL
);