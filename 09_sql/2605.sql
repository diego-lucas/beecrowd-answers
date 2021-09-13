SELECT
    products.name,
    providers.name
FROM
    products
    JOIN providers ON (providers.id = products.id_providers)
WHERE
    products.id_categories = 6