-- CREATE DATABASE online_store_db;

CREATE TABLE IF NOT EXISTS
	item_types(
		"id" SERIAL PRIMARY KEY,
		item_type_name VARCHAR(50)
	);


CREATE TABLE IF NOT EXISTS
	items(
		"id" SERIAL PRIMARY KEY,
		item_name VARCHAR(50),
		item_type_id INT,
		CONSTRAINT fk_items_item_types
			FOREIGN KEY (item_type_id)
				REFERENCES item_types("id")
	);


CREATE TABLE IF NOT EXISTS
	cities(
		"id" SERIAL PRIMARY KEY,
		city_name VARCHAR(50)
	);


CREATE TABLE IF NOT EXISTS
	customers(
		"id" SERIAL PRIMARY KEY,
		customer_name VARCHAR(100),
		birthday DATE,
		city_id INTEGER,
		CONSTRAINT fk_customers_cities
			FOREIGN KEY (city_id)
				REFERENCES cities("id")
	);


CREATE TABLE IF NOT EXISTS
	orders(
		"id" SERIAL PRIMARY KEY,
		customer_id INTEGER,
		CONSTRAINT fk_orders_customers
			FOREIGN KEY (customer_id)
				REFERENCES customers("id")
	);


CREATE TABLE IF NOT EXISTS
	order_items(
		order_id INTEGER,
		item_id INTEGER,
		CONSTRAINT pk_order_items PRIMARY KEY (order_id, item_id),
		CONSTRAINT fk_order_items_orders
			FOREIGN KEY (order_id)
				REFERENCES orders("id"),
		CONSTRAINT fk_order_items_items
			FOREIGN KEY (item_id)
				REFERENCES items("id")
	);