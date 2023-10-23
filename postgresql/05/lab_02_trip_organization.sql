SELECT
	v.driver_id,
	v.vehicle_type,
	CONCAT(d.first_name, ' ', d.last_name) AS driver_name
FROM
	vehicles AS v JOIN
 		campers AS d ON
			v.driver_id = d.id;