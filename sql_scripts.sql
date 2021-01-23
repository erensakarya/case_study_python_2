SELECT * FROM TV_SHOWS ts;
---------------------

select * from "CAST" order by popularity desc;
----------------------------------

select * from CAST order by popularity desc LIMIT 10;
--------------------------------

SELECT c1.id, c1.name, c1.gender, c1.known_for_department, c1.popularity, c1.tv_show_id_played,
	CASE tv_show_id_played
	WHEN 1408 THEN "House"
	WHEN 2316 THEN "The Office"
	WHEN 76479 THEN "The Boys"
    END AS "tv_show_name_played"
FROM cast c1;
--------------------------------------------------

SELECT
	ROW_NUMBER() OVER(ORDER BY count(popularity) desc) AS "Popularity Order",
	name as "Actress/Actor's Name",
	CASE Gender
	WHEN 1 THEN "Female"
    ELSE "Male"
    END AS "Gender"
FROM cast
GROUP BY popularity
ORDER BY popularity desc
LIMIT 10;
-----------------------------------------------------
SELECT * FROM(
		SELECT
			id as "Person_Id",
			name as 'Name',
			CASE Gender
			WHEN 1 THEN "Female"
		    ELSE "Male"
		    END AS "Gender",
		    known_for_department as 'Known_For',
		    popularity as Popularity,
		    CASE tv_show_id_played
			WHEN 1408 THEN "House"
			WHEN 2316 THEN "The Office"
			WHEN 76479 THEN "The Boys"
    		END AS "TV_Show_Name_Involved"
		FROM cast c1
	UNION 
		SELECT
			id as "Person_Id",
			name as 'Name',
			CASE Gender
			WHEN 1 THEN "Female"
		    ELSE "Male"
		    END AS "Gender",
		    known_for_department as 'Known_For',
		    popularity as Popularity,
		    CASE tv_show_id_involved
			WHEN 1408 THEN "House"
			WHEN 2316 THEN "The Office"
			WHEN 76479 THEN "The Boys"
    		END AS "TV_Show_Name_Involved"
		FROM crew c2
) c3
ORDER BY c3.popularity desc;

select * from cast;

select * from (
SELECT c1.name, c1.popularity, c1.known_for_department 
  FROM cast c1
UNION
 SELECT c2.name, c2.popularity, c2.known_for_department
   FROM crew c2) c3
WHERE c3.known_for_department in ('Acting', 'Directing', 'Writing')
ORDER BY popularity desc;




SELECT c2.id, c2.name, c2.gender, c2.known_for_department, c2.popularity, c2.tv_show_id_involved,
	CASE c2.tv_show_id_involved
	WHEN 1408 THEN "House"
	WHEN 2316 THEN "The Office"
	WHEN 76479 THEN "The Boys"
    END AS "tv_show_name_involved"
FROM crew c2;
-----------------------------------------------------------

SELECT c2.id, c2.name, c2.gender, c2.known_for_department, c2.popularity, c2.tv_show_id_involved,
	CASE c2.tv_show_id_involved
	WHEN 1408 THEN "House"
	WHEN 2316 THEN "The Office"
	WHEN 76479 THEN "The Boys"
    END AS "tv_show_name_involved"
FROM crew c2
WHERE c2.known_for_department = 'Directing';
---------------------------------------------------------------


select count(c2.name) as count_of_directed_movies, c2.name from crew c2
where c2.known_for_department = 'Directing'
group by c2.name
-----------------------------------------------------

select * from directors;
----------------------------------------------------

SELECT
	CASE d.director_id
	WHEN 9032 THEN "Bryan Singer"
	WHEN 1533790 THEN "Ira Hurvitz"
	WHEN 29009 THEN "Ken Kwapis"
	WHEN 1225933 THEN "Philip Sgriccia"
    END AS "Director Name",
    d.tv_show_names as "Series",
    d.episode_count as "Episodes Directed"
FROM directors d;
-----------------------------------------------------


select *
from (((select *, row_number() over (partition by known_for_department order by popularity desc) as r from cast) a where r <= 5 and known_for_department in ('Acting')),
((select *, row_number() over (partition by known_for_department order by popularity desc) as r from crew) a where r <= 5 and known_for_department in ('Directing')));
--------------------------------------------------- 


select name as "Directing"
from (
    select *, row_number() over (partition by known_for_department order by popularity desc) as r
    from crew
    ) a 
where r <= 5
  and known_for_department in ('Directing');
----------------------------------------------------
 
select name as "Writing"
from (
    select *, row_number() over (partition by known_for_department order by popularity desc) as r
    from crew
    ) a 
where r <= 5
  and known_for_department in ('Writing');
---------------------------------------------------
 

SELECT * FROM (
(select r1 as r1, name as "Acting"
from (select *, row_number() over (partition by known_for_department order by popularity desc) as r1 from cast) a where r1 <= 5 and known_for_department in ('Acting')) t1,
(select r2 as r2, name as "Directing"
from (select *, row_number() over (partition by known_for_department order by popularity desc) as r2 from crew) b where r2 <= 5 and known_for_department in ('Directing')) t2 ) 
WHERE  t1.r1 = t2.r2 ;


SELECT * FROM (
(select r1 as r1, name as "Acting"
from (select *, row_number() over (partition by known_for_department order by popularity desc) as r1 from cast) a where r1 <= 5 and known_for_department in ('Acting')) t1
LEFT OUTER JOIN
(select r2 as r2, name as "Directing"
from (select *, row_number() over (partition by known_for_department order by popularity desc) as r2 from crew) b where r2 <= 5 and known_for_department in ('Directing')) t2
ON t1.r1=t2.r2) 

----------------------------------------------------------

 
 
select * from (
SELECT c1.name, c1.popularity, c1.known_for_department 
  FROM cast c1
UNION
 SELECT c2.name, c2.popularity, c2.known_for_department
   FROM crew c2) c3
WHERE c3.known_for_department in ('Acting', 'Directing', 'Writing')
ORDER BY popularity desc;




SELECT c1.name, c1.popularity, c1.known_for_department 
  FROM cast c1 order by 2 desc;

SELECT row_number() over (partition by known_for_department order by popularity desc) as 
'popularity order', name as 'ACTING' FROM cast where known_for_department = 'Acting' order by popularity desc LIMIT 5;

SELECT row_number() over (partition by known_for_department order by popularity desc) as 
'popularity order', name as 'DIRECTING' FROM crew where known_for_department = 'Directing' order by popularity desc LIMIT 5;


SELECT row_number() over (partition by known_for_department order by popularity desc) as 
'popularity order', name as 'WRITING' FROM crew where known_for_department = 'Writing' order by popularity desc LIMIT 5;


---------------------------------------------Q4------------------------------------------------------------------
select s1.'Popularity Order', ACTING, DIRECTING, WRITING from 
(SELECT row_number() over (partition by known_for_department order by popularity desc) as 'Popularity Order', 
		name as 'ACTING' FROM cast where known_for_department = 'Acting' order by popularity desc LIMIT 5)s1
		LEFT OUTER JOIN 
(SELECT row_number() over (partition by known_for_department order by popularity desc) as 'Popularity Order', 
		name as 'DIRECTING' FROM crew where known_for_department = 'Directing' order by popularity desc LIMIT 5)s2
		ON s1.'Popularity Order' = s2.'Popularity Order'
		LEFT OUTER JOIN
(SELECT row_number() over (partition by known_for_department order by popularity desc) as 'Popularity Order', 
		name as 'WRITING' FROM crew where known_for_department = 'Writing' order by popularity desc LIMIT 5)s3
		ON s1.'Popularity Order' = s3.'Popularity Order';
------------------------------------------------------------------------------------------------------------------


