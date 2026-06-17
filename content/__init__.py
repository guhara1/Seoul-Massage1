# 전체 페이지 목록 집계
from . import main, districts, dongs, stations, zones, info

PAGES = (
    [main.PAGE]
    + districts.PAGES
    + dongs.PAGES
    + stations.PAGES
    + zones.PAGES
    + info.PAGES
)
