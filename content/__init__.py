# 전체 페이지 목록 집계
# 1) 자동 생성 행정동 모듈을 먼저 불러와 링크 레지스트리에 등록한다.
#    (districts 가 import 시점에 dong_nav_section 을 호출하므로 그 전에 병합)
from . import dongs_gen
from .site import register_dong_pages

register_dong_pages(dongs_gen.ALL_DONG_SLUGS)

# 레지스트리가 모두 채워진 뒤 자동 생성 페이지를 만든다(내부링크 sibling 해석).
dongs_gen.PAGES = dongs_gen.build()

# 2) 나머지 페이지 모듈 import (dongs/districts 는 등록된 레지스트리를 사용)
from . import main, districts, dongs, stations, zones, info

PAGES = (
    [main.PAGE]
    + districts.PAGES
    + dongs.PAGES
    + dongs_gen.PAGES
    + stations.PAGES
    + zones.PAGES
    + info.PAGES
)
