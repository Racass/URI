SELECT T0.id, T0.name FROM products T0
INNER JOIN categories T1 ON T0.id_categories = T1.id
WHERE T1.name LIKE 'super%'
