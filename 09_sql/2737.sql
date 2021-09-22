(
    SELECT
        name,
        customers_number
    FROM
        public.lawyers
    WHERE
        customers_number = (
            SELECT
                MIN(customers_number)
            FROM
                public.lawyers
        )
        OR customers_number = (
            SELECT
                MAX(customers_number)
            FROM
                public.lawyers
        )
    ORDER BY
        2 DESC
)
UNION
ALL
SELECT
    'Average',
    AVG(customers_number) :: INTEGER
FROM
    public.lawyers