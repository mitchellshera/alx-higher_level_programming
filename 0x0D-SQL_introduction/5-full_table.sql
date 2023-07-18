-- Retrieve the full table description from information_schema
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
    AND TABLE_NAME = 'first_table';
