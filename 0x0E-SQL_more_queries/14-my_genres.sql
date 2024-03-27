-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)
-- A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- >> The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- >> Each record should display: tv_genres.name
-- >> Results must be sorted in ascending order by the genre name
-- ---------
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
    SELECT tv_genres.name
      FROM tv_genres
INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
     WHERE tv_shows.title = "Dexter"
  ORDER BY tv_genres.name ASC;