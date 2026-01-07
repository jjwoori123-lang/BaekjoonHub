-- 코드를 입력하세요
SELECT date_format(SALES_DATE, "%Y-%m-%d") as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT 
from ONLINE_SALE 
where SALES_DATE like "2022-03%"

Union all

SELECT date_format(SALES_DATE, "%Y-%m-%d") as SALES_DATE, PRODUCT_ID, null as USER_ID, SALES_AMOUNT 
from OFFLINE_SALE  
where SALES_DATE like "2022-03%"
ORDER BY SALES_DATE asc, PRODUCT_ID asc, USER_ID asc