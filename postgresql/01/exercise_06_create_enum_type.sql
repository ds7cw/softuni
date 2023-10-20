CREATE TYPE type_mood AS ENUM ('happy', 'relaxed', 'stressed', 'sad');

ALTER TABLE IF EXISTS minions_info
ADD COLUMN mood type_mood NOT NULL;