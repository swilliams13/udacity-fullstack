import psycopg2

conn = psycopg2.connect("dbname=news")

cursor = conn.cursor()

query1 = ("select views, title from "
          "(select count(*) as views, path from log group by path) as "
          "log_views, articles "
          "where log_views.path like concat('%', articles.slug) "
          "order by views desc limit 3;")

query2 = ("select name, sum(views) as totalViews from articles, authors, "
          "(select count(*) as views, path from log group by path) as "
          "log_views where articles.author = authors.id and log_views.path "
          "like concat('%', articles.slug) group by name order by "
          "totalViews desc;")

query3 = ("select round((num_errors/num_total)*100,1) as percentage, "
          "to_char(total.date, 'FMMonth DD, YYYY') as date from "
          "(select cast(count(id) as decimal) as num_errors, "
          "date_trunc('day',time) as date from log where "
          "(status LIKE '4%' OR status LIKE '5%') group by date) as errors, "
          "(select cast(count(id) as decimal) as num_total, "
          "date_trunc('day',time) as date from log group by date) as total "
          "where total.date = errors.date and "
          "((num_errors/num_total)*100) > 1.0;")

cursor.execute(query1)
results = cursor.fetchall()

print "\nMOST POPULAR THREE ARTICLES OF ALL TIME"
for result in results:
    print '    "{}" - {} views'.format(result[1], result[0])

cursor.execute(query2)
results = cursor.fetchall()
print "\nMOST POPULAR ARTICLE AUTHORS OF ALL TIME"
for result in results:
    print '    {} - {} views'.format(result[0], result[1])

cursor.execute(query3)
results = cursor.fetchall()
print "\nDAYS WITH MORE THAN 1% REQUEST ERRORS"
for result in results:
    print '    {} - {}% errors'.format(result[1], result[0])

cursor.close()
conn.close()
