-- 코드를 작성해주세요
select count(*) as count
from ECOLI_DATA 
where GENOTYPE & 2 = 0 and (GENOTYPE & 4 >0 or GENOTYPE & 1 >0)