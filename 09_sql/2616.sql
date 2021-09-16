SELECT
    customers.id,
    customers.name
FROM
    customers FULL
    JOIN locations ON (customers.id = locations.id_customers)
GROUP BY
    customers.id,
    customers.name
HAVING
    COUNT(locations.locations_date) = 0
ORDER BY
    customers.id