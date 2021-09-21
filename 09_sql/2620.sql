SELECT
    customers.name,
    orders.id
FROM
    customers
    JOIN orders ON (customers.id = orders.id_customers)
WHERE
    orders.orders_date <= '2021-06-30'