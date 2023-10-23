CREATE TABLE IF NOT EXISTS
	clients(
		"id" SERIAL PRIMARY KEY,
		"name" VARCHAR(10)
	);

CREATE TABLE IF NOT EXISTS
	employees(
		"id" SERIAL PRIMARY KEY,
		first_name VARCHAR(30),
		last_name VARCHAR(30),
		project_id INTEGER
	);

CREATE TABLE IF NOT EXISTS
	projects(
		"id" SERIAL PRIMARY KEY,
		client_id INTEGER,
		project_lead_id INTEGER,
		CONSTRAINT fk_projects_clients_client_id
			FOREIGN KEY (client_id)
				REFERENCES clients("id"),
		CONSTRAINT fk_projects_employees_proj_lead_id
			FOREIGN KEY (project_lead_id)
				REFERENCES employees("id")
	);
	
ALTER TABLE IF EXISTS
	employees
ADD CONSTRAINT fk_employees_projects_project_id
			FOREIGN KEY (project_id)
				REFERENCES projects("id");