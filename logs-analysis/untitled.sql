--1.

SELECT views, title FROM articles,
(SELECT COUNT(id) as views,
REPLACE(path, '/article/', '') AS log_slug
FROM log
WHERE status = '200 OK' and NOT(path='/')
GROUP BY log_slug) as article_views
WHERE slug = log_slug
ORDER BY views DESC
LIMIT 3;

--2.

SELECT name, SUM(views) AS TotalViews FROM articles, authors,
(SELECT COUNT(id) as views,
REPLACE(path, '/article/', '') AS log_slug
FROM log
WHERE status = '200 OK' and NOT(path='/')
GROUP BY log_slug) as article_views
WHERE slug = log_slug
AND author = authors.id
GROUP BY name
ORDER BY TotalViews DESC;

--3.

SELECT DISTINCT status, time from log group by time, status
LIMIT 25;

SELECT TO_Char(time, 'YYYY-MM-DD') from log
LIMIT 25;