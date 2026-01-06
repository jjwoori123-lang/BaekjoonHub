-- 코드를 작성해주세요
select a.id, a.genotype, b.genotype as PARENT_GENOTYPE from ECOLI_DATA a, ECOLI_DATA b
where a.parent_id = b.id and a.genotype & b.genotype = b.genotype order by a.id