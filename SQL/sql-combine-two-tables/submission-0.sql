-- Write your query below
SELECT first_name, last_name, city, state 
FROM person p
LEFT JOIN address a ON a.person_id = p.person_id;