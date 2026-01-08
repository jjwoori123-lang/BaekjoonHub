select distinct d.id, d.email, d.first_name, d.last_name
from SKILLCODES s
join DEVELOPERS d on s.CODE & d.SKILL_CODE = s.CODE
where s.name in ("Python ", "C#")
order by d.id
