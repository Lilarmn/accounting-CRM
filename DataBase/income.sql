CREATE DEFINER=`root`@`localhost` PROCEDURE `Income_date`(in d1 varchar(255),in d2 varchar(255) ,out res bigint)
BEGIN
	if d1 = '*' then
		select sum(s.price - k.buy) INTO res from sales as s
		inner join (SELECT * FROM accessories 
					UNION ALL
					SELECT * FROM airpods 
					UNION ALL
					SELECT * FROM electrical_tools 
					UNION ALL
					SELECT * FROM speaker_and_headsets 
					UNION ALL
					SELECT * FROM watchs
					UNION ALL 
					select * from phones) as k on k.ID = s.ID;
	else
		select sum(s.price - k.buy) INTO res from sales as s
		inner join (SELECT * FROM accessories 
				UNION ALL
				SELECT * FROM airpods 
				UNION ALL
				SELECT * FROM electrical_tools 
				UNION ALL
				SELECT * FROM speaker_and_headsets 
				UNION ALL
				SELECT * FROM watchs
				UNION ALL 
				select * from phones) as k on k.ID = s.ID
		where s.date between d1 and d2;
    end if;
END