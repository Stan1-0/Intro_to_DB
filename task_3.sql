SELECT 
    table_schema AS "Database Name",
    table_name AS "Table Name"
FROM 
    information_schema.tables
WHERE 
    table_schema = LOWER(?)
ORDER BY 
    table_schema, table_name;