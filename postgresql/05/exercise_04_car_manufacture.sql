-- CREATE DATABASE car_manufacture_db

CREATE TABLE IF NOT EXISTS
	manufacturers(
		"id" SERIAL PRIMARY KEY,
		"name" VARCHAR(50)
	);


CREATE TABLE IF NOT EXISTS
	models(
		"id" INTEGER GENERATED ALWAYS AS IDENTITY(START WITH 1000 INCREMENT BY 1) PRIMARY KEY,
		model_name VARCHAR(50),
		manufacturer_id INTEGER,
		CONSTRAINT fk_models_manufacturers
			FOREIGN KEY (manufacturer_id)
				REFERENCES manufacturers("id")
	);


CREATE TABLE IF NOT EXISTS
	production_years(
		"id" SERIAL PRIMARY KEY,
		established_on DATE NOT NULL,
		manufacturer_id INTEGER,
		CONSTRAINT fk_production_years_manufacturers
			FOREIGN KEY (manufacturer_id)
				REFERENCES manufacturers("id")
	);


INSERT INTO
	manufacturers("name")
VALUES
	('BMW'),
	('Tesla'),
	('Lada');

INSERT INTO
	models(model_name, manufacturer_id)
VALUES
	('X1', 1),
	('i6', 1),
	('Model S', 2),
	('Model X', 2),
	('Model 3', 2),
	('Nova', 3);

INSERT INTO
	production_years(established_on, manufacturer_id)
VALUES
	('1916-03-01'::DATE, 1),
	('2003-01-01'::DATE, 2),
	('1966-05-01'::DATE, 3);
