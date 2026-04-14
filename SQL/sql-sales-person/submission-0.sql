-- Write your query below
SELECT name
FROM sales_person s
LEFT JOIN orders o 
    ON o.sales_id = s.sales_id
    AND o.com_id = (
        SELECT c.com_id
        FROM company c
        WHERE c.name = 'CRIMSON'
        )
WHERE o.com_id IS NULL;