select concat(QUARTER(DIFFERENTIATION_DATE), 'Q') as QUARTER, count(id) as ECOLI_COUNT
from ECOLI_DATA 
group by QUARTER
order by QUARTER