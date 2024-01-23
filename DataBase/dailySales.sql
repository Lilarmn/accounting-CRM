CREATE DEFINER=`root`@`localhost` PROCEDURE `DailySales`(in d1 varchar(255) , out res bigint)
BEGIN
	if d1 = '*' then
		SELECT SUM(price) INTO res FROM sales;
	else
		SELECT SUM(price) INTO res FROM sales
        where `date`= d1;
        
	end if;
END