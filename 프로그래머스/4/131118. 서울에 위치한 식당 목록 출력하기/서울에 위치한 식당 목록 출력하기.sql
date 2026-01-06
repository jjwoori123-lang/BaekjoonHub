-- 코드를 입력하세요
SELECT a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS, round(avg(b.REVIEW_SCORE),2) as SCORE
from REST_INFO a
join REST_REVIEW b on
b.REST_ID = a.REST_ID
where a.address like "서울%"
GROUP BY a.REST_ID
order by score desc, FAVORITES desc
