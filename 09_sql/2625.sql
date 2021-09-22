SELECT
    REGEXP_REPLACE(
        cpf,
        '([0-9]{3})([0-9]{3})([0-9]{3})',
        '\1.\2.\3-'
    )
FROM
    natural_person