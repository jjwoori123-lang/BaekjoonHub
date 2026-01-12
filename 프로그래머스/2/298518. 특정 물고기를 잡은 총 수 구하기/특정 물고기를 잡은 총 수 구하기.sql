select count(a.fish_type) as fish_count
from FISH_INFO  a
join FISH_NAME_INFO b on a.FISH_TYPE = b.FISH_TYPE
where b.FISH_NAME = "bass" or b.FISH_NAME = "snapper"