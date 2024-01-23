CREATE DEFINER=`root`@`localhost` PROCEDURE `phoneSumBuy`(in d1 varchar(255) , in d2 varchar(255) , out res bigint)
BEGIN
	if d1 = '*' then
		SELECT SUM(buy) INTO res FROM phones;
	else
		SELECT SUM(buy) INTO res FROM phones
        where `date` between d1 and d2;
        
	end if;
END