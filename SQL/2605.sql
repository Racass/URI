SELECT T0.name, T1.name FROM products T0
INNER JOIN providers T1 ON T0.id_providers = T1.id
WHERE id_categories = 6