SELECT T0.name, sum(T1.amount) as sum FROM categories T0 
INNER JOIN products T1 ON T0.id = T1.id_categories

GROUP BY T0.name
