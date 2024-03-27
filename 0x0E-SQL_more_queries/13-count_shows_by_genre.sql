-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)
-- >> script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- >> Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- >> First column must be called genre
-- >> Second column must be called number_of_shows
-- >> Don’t display a genre that doesn’t have any shows linked
-- >> Results must be sorted in descending order by the number of shows linked
-- >> You can use only one SELECT statement
-- -----------
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
SELECT tv_genres.name AS genre, COUNT(*) AS 'number_of_shows'
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
