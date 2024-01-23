CREATE DEFINER=`root`@`localhost` PROCEDURE `repSumBuy`(IN beginDate VARCHAR(255), IN endDate VARCHAR(255), OUT result bigint)
BEGIN

	if beginDate = '*' then
		select sum(buy) INTO result from (
		SELECT buy FROM accessories 
		UNION ALL
		SELECT buy FROM airpods 
		UNION ALL
		SELECT buy FROM electrical_tools 
		UNION ALL
		SELECT buy FROM speaker_and_headsets 
		UNION ALL
		SELECT buy FROM watchs) k ;
        
	else
		select sum(buy) INTO result from (
		SELECT buy FROM accessories where date between beginDate and endDate
		UNION ALL
		SELECT buy FROM airpods where date between beginDate and endDate
		UNION ALL
		SELECT buy FROM electrical_tools where date between beginDate and endDate
		UNION ALL
		SELECT buy FROM speaker_and_headsets where date between beginDate and endDate
		UNION ALL
		SELECT buy FROM watchs where date between beginDate and endDate) k ;
        
	end if;
END