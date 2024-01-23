CREATE DEFINER=`root`@`localhost` PROCEDURE `repSumQuantity`(IN beginDate VARCHAR(255), IN endDate VARCHAR(255), OUT result bigint)
BEGIN
    if beginDate = '*' then
		select sum(quantity) INTO result from (
		SELECT quantity FROM accessories 
		UNION ALL
		SELECT quantity FROM airpods 
		UNION ALL
		SELECT quantity FROM electrical_tools 
		UNION ALL
		SELECT quantity FROM speaker_and_headsets 
		UNION ALL
		SELECT quantity FROM watchs) k ;
        
	else
		select sum(quantity) INTO result from (
		SELECT quantity FROM accessories where date between beginDate and endDate
		UNION ALL
		SELECT quantity FROM airpods where date between beginDate and endDate
		UNION ALL
		SELECT quantity FROM electrical_tools where date between beginDate and endDate
		UNION ALL
		SELECT quantity FROM speaker_and_headsets where date between beginDate and endDate
		UNION ALL
		SELECT quantity FROM watchs where date between beginDate and endDate) k ;
        
	end if;
END