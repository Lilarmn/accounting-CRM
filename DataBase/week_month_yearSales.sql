CREATE DEFINER=`root`@`localhost` PROCEDURE `week_month_yearSales`(in d1 varchar(255) , in d2 varchar(255) , out res bigint)
BEGIN
	if d1 = '*' then
		SELECT SUM(price) INTO res FROM sales;
	else
		SELECT SUM(price) INTO res FROM sales
        where `date` between d1 and d2;
        
	end if;
END