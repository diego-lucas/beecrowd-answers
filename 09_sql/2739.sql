SELECT
    name,
    EXTRACT(day FROM payday)::INTEGER
FROM
    loan