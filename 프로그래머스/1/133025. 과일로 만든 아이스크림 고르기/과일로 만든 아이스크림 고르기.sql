SELECT a.FLAVOR as FLAVOR
from FIRST_HALF a 
join ICECREAM_INFO b on a.flavor = b.flavor 
where a.total_order > 3000 
and b.INGREDIENT_TYPE = 'fruit_based' 
order by a.TOTAL_ORDER desc