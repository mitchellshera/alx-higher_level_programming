-- Retrieve privileges of MySQL users user_0d_1 and user_0d_2 on localhost server

-- Select the specific columns for privileges from mysql.user table
SELECT User, Host, Grant_priv, Super_priv, Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv

-- Filter the query based on the specified users and host
FROM mysql.user
WHERE User IN ('user_0d_1', 'user_0d_2')
  AND Host = 'localhost';
