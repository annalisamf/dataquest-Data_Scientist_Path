## 3. The With Clause ##

WITH track_info AS
    (                
     SELECT
         p.playlist_id playlist_id ,
         p.name playlist_name,
         pt.track_id,
         t.milliseconds / 1000 length_seconds
     FROM playlist p
     LEFT JOIN playlist_track pt ON p.playlist_id = pt.playlist_id
     LEFT JOIN track t ON pt.track_id = t.track_id
    )

SELECT playlist_id, playlist_name, COUNT(track_id) number_of_tracks, SUM(length_seconds)length_seconds FROM track_info
GROUP BY 1, 2
ORDER BY 1;

## 4. Creating Views ##

CREATE VIEW chinook.customer_gt_90_dollars AS
    SELECT c.* 
    FROM customer c
    LEFT JOIN invoice i ON i.customer_id=c.customer_id
    GROUP BY 1
    HAVING SUM(i.total) > 90;

SELECT * FROM chinook.customer_gt_90_dollars;

## 5. Combining Rows With Union ##

SELECT * FROM customer_usa
UNION
SELECT * FROM customer_gt_90_dollars;

## 6. Combining Rows Using Intersect and Except ##

SELECT e.first_name || " " || e.last_name employee_name,
COUNT(c.customer_id) customers_usa_gt_90
FROM employee e
LEFT JOIN 
    (SELECT * from customer_usa
    INTERSECT
    SELECT * from customer_gt_90_dollars) c 
    ON c.support_rep_id=e.employee_id
WHERE e.title = "Sales Support Agent"
GROUP BY 1
ORDER BY 1;

## 7. Multiple Named Subqueries ##

WITH
    india AS
        (
        SELECT * FROM customer
        WHERE country = "India"
        ),
    purchases AS
        (
         SELECT 
            customer_id, 
            SUM(total) total 
         FROM invoice
         GROUP BY 1
        )

SELECT 
    india.first_name || " " || india.last_name customer_name,
    p.total total_purchases
FROM india
INNER JOIN purchases p ON p.customer_id=india.customer_id
ORDER BY 1;


## 8. Challenge: Each Country's Best Customer ##

WITH max_purchase AS
    (
        SELECT customer_id, SUM(total) total 
        FROM invoice
        GROUP BY 1
    )


SELECT 
    c.country country,
    c.first_name || " " || c.last_name customer_name,
    max_purchase.total total_purchased
FROM customer c
INNER JOIN max_purchase ON max_purchase.customer_id=c.customer_id
GROUP BY 1 HAVING total_purchased=MAX(total_purchased)
ORDER BY 1;