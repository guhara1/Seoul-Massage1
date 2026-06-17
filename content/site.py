# 사이트 공통 설정
BASE_URL = "https://seoul-massage1.pages.dev"

BRAND = "간다GO"
BRAND_MARK = "GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 25개 자치구 (slug, 한글명)
DISTRICTS = [
    ("gangnam-gu-chuljangmassage", "강남구"),
    ("gangdong-gu-chuljangmassage", "강동구"),
    ("gangbuk-gu-chuljangmassage", "강북구"),
    ("gangseo-gu-chuljangmassage", "강서구"),
    ("gwanak-gu-chuljangmassage", "관악구"),
    ("gwangjin-gu-chuljangmassage", "광진구"),
    ("guro-gu-chuljangmassage", "구로구"),
    ("geumcheon-gu-chuljangmassage", "금천구"),
    ("nowon-gu-chuljangmassage", "노원구"),
    ("dobong-gu-chuljangmassage", "도봉구"),
    ("dongdaemun-gu-chuljangmassage", "동대문구"),
    ("dongjak-gu-chuljangmassage", "동작구"),
    ("mapo-gu-chuljangmassage", "마포구"),
    ("seodaemun-gu-chuljangmassage", "서대문구"),
    ("seocho-gu-chuljangmassage", "서초구"),
    ("seongdong-gu-chuljangmassage", "성동구"),
    ("seongbuk-gu-chuljangmassage", "성북구"),
    ("songpa-gu-chuljangmassage", "송파구"),
    ("yangcheon-gu-chuljangmassage", "양천구"),
    ("yeongdeungpo-gu-chuljangmassage", "영등포구"),
    ("yongsan-gu-chuljangmassage", "용산구"),
    ("eunpyeong-gu-chuljangmassage", "은평구"),
    ("jongno-gu-chuljangmassage", "종로구"),
    ("jung-gu-chuljangmassage", "중구"),
    ("jungnang-gu-chuljangmassage", "중랑구"),
]

# 메뉴용 핵심 역세권 21개
STATIONS_MENU = [
    ("gangnam-station-chuljangmassage", "강남역"),
    ("yeoksam-station-chuljangmassage", "역삼역"),
    ("seolleung-station-chuljangmassage", "선릉역"),
    ("samseong-station-chuljangmassage", "삼성역"),
    ("jamsil-station-chuljangmassage", "잠실역"),
    ("hongik-univ-station-chuljangmassage", "홍대입구역"),
    ("hapjeong-station-chuljangmassage", "합정역"),
    ("yeouido-station-chuljangmassage", "여의도역"),
    ("yeongdeungpo-station-chuljangmassage", "영등포역"),
    ("seoul-station-chuljangmassage", "서울역"),
    ("yongsan-station-chuljangmassage", "용산역"),
    ("wangsimni-station-chuljangmassage", "왕십리역"),
    ("geondae-entrance-station-chuljangmassage", "건대입구역"),
    ("sinchon-station-chuljangmassage", "신촌역"),
    ("sadang-station-chuljangmassage", "사당역"),
    ("gyodae-station-chuljangmassage", "교대역"),
    ("gosok-terminal-station-chuljangmassage", "고속터미널역"),
    ("jongno3ga-station-chuljangmassage", "종로3가역"),
    ("euljiro-entrance-station-chuljangmassage", "을지로입구역"),
    ("city-hall-station-chuljangmassage", "시청역"),
    ("gimpo-airport-station-chuljangmassage", "김포공항역"),
]

# 생활권 10개 (slug, 한글명)
ZONES = [
    ("gangnam-zone-chuljangmassage", "강남역 생활권"),
    ("jamsil-songpa-zone-chuljangmassage", "잠실·송파 생활권"),
    ("hongdae-hapjeong-zone-chuljangmassage", "홍대·합정 생활권"),
    ("yeouido-zone-chuljangmassage", "여의도 업무지구"),
    ("seoul-yongsan-zone-chuljangmassage", "서울역·용산 생활권"),
    ("jongno-gwanghwamun-zone-chuljangmassage", "종로·광화문 생활권"),
    ("seongsu-wangsimni-zone-chuljangmassage", "성수·왕십리 생활권"),
    ("guro-digital-zone-chuljangmassage", "구로디지털단지"),
    ("gimpo-magok-zone-chuljangmassage", "김포공항·마곡 생활권"),
    ("nowon-sanggye-zone-chuljangmassage", "노원·상계 생활권"),
]


def district_url(slug):
    return f"/seoul/{slug}/"


def station_url(slug):
    return f"/seoul/{slug}/"


def zone_url(slug):
    return f"/seoul/{slug}/"


def dong_url(slug):
    return f"/seoul/{slug}-chuljangmassage/"


# 자치구별 통합 행정동 (번호 동은 대표 동으로 통합)
DISTRICT_DONGS = {
    "gangnam-gu-chuljangmassage": ["신사동", "논현동", "압구정동", "청담동", "삼성동", "대치동", "역삼동", "도곡동", "개포동", "일원동", "수서동", "세곡동"],
    "gangdong-gu-chuljangmassage": ["천호동", "성내동", "길동", "둔촌동", "암사동", "명일동", "고덕동", "상일동", "강일동"],
    "gangbuk-gu-chuljangmassage": ["미아동", "번동", "수유동", "우이동", "인수동", "삼양동"],
    "gangseo-gu-chuljangmassage": ["화곡동", "마곡동", "발산동", "등촌동", "염창동", "가양동", "공항동", "방화동", "우장산동"],
    "gwanak-gu-chuljangmassage": ["봉천동", "신림동", "남현동", "낙성대동", "서원동", "미성동", "난곡동"],
    "gwangjin-gu-chuljangmassage": ["구의동", "자양동", "화양동", "광장동", "중곡동", "능동", "군자동"],
    "guro-gu-chuljangmassage": ["구로동", "신도림동", "가리봉동", "고척동", "개봉동", "오류동", "온수동", "항동", "천왕동"],
    "geumcheon-gu-chuljangmassage": ["가산동", "독산동", "시흥동"],
    "nowon-gu-chuljangmassage": ["상계동", "중계동", "하계동", "월계동", "공릉동"],
    "dobong-gu-chuljangmassage": ["창동", "쌍문동", "방학동", "도봉동"],
    "dongdaemun-gu-chuljangmassage": ["전농동", "답십리동", "장안동", "청량리동", "회기동", "휘경동", "이문동", "제기동", "용두동", "신설동"],
    "dongjak-gu-chuljangmassage": ["노량진동", "상도동", "흑석동", "사당동", "대방동", "신대방동", "동작동", "본동"],
    "mapo-gu-chuljangmassage": ["공덕동", "아현동", "도화동", "용강동", "대흥동", "염리동", "신수동", "서교동", "합정동", "망원동", "연남동", "성산동", "상암동"],
    "seodaemun-gu-chuljangmassage": ["충정로", "북아현동", "신촌동", "대현동", "연희동", "홍제동", "홍은동", "남가좌동", "북가좌동", "천연동"],
    "seocho-gu-chuljangmassage": ["서초동", "잠원동", "반포동", "방배동", "양재동", "내곡동", "우면동"],
    "seongdong-gu-chuljangmassage": ["왕십리동", "행당동", "금호동", "옥수동", "성수동", "응봉동", "마장동", "사근동", "용답동", "송정동"],
    "seongbuk-gu-chuljangmassage": ["성북동", "돈암동", "삼선동", "안암동", "보문동", "정릉동", "길음동", "종암동", "월곡동", "장위동", "석관동"],
    "songpa-gu-chuljangmassage": ["잠실동", "신천동", "송파동", "석촌동", "삼전동", "가락동", "문정동", "장지동", "거여동", "마천동", "방이동", "오금동", "풍납동"],
    "yangcheon-gu-chuljangmassage": ["목동", "신정동", "신월동"],
    "yeongdeungpo-gu-chuljangmassage": ["영등포동", "여의도동", "당산동", "문래동", "양평동", "신길동", "대림동", "도림동"],
    "yongsan-gu-chuljangmassage": ["한강로동", "이태원동", "한남동", "청파동", "효창동", "용문동", "원효로동", "이촌동", "서빙고동", "보광동", "남영동", "후암동", "용산동"],
    "eunpyeong-gu-chuljangmassage": ["불광동", "응암동", "녹번동", "갈현동", "구산동", "대조동", "역촌동", "신사동", "증산동", "수색동", "진관동"],
    "jongno-gu-chuljangmassage": ["청운효자동", "사직동", "삼청동", "부암동", "평창동", "무악동", "교남동", "가회동", "종로1·2·3·4가동", "종로5·6가동", "이화동", "혜화동", "창신동", "숭인동"],
    "jung-gu-chuljangmassage": ["소공동", "회현동", "명동", "필동", "장충동", "광희동", "을지로동", "신당동", "다산동", "약수동", "청구동", "동화동", "황학동", "중림동"],
    "jungnang-gu-chuljangmassage": ["면목동", "상봉동", "중화동", "묵동", "망우동", "신내동"],
}

# 상세 페이지가 있는 행정동 (자치구 slug → {행정동명: 페이지 slug})
DONG_PAGES = {
    "gangnam-gu-chuljangmassage": {"역삼동": "yeoksam-dong", "삼성동": "samseong-dong", "청담동": "cheongdam-dong", "논현동": "nonhyeon-dong", "대치동": "daechi-dong"},
    "songpa-gu-chuljangmassage": {"잠실동": "jamsil-dong", "문정동": "munjeong-dong", "가락동": "garak-dong", "방이동": "bangi-dong"},
    "mapo-gu-chuljangmassage": {"서교동": "seogyeo-dong", "합정동": "hapjeong-dong", "공덕동": "gongdeok-dong", "상암동": "sangam-dong"},
    "yeongdeungpo-gu-chuljangmassage": {"여의도동": "yeouido-dong", "영등포동": "yeongdeungpo-dong", "당산동": "dangsan-dong"},
    "yongsan-gu-chuljangmassage": {"한강로동": "hangang-ro-dong", "이태원동": "itaewon-dong", "한남동": "hannam-dong"},
    "seongdong-gu-chuljangmassage": {"성수동": "seongsu-dong", "왕십리동": "wangsimni-dong", "옥수동": "oksu-dong"},
    "seocho-gu-chuljangmassage": {"서초동": "seocho-dong", "반포동": "banpo-dong", "방배동": "bangbae-dong"},
    "gangseo-gu-chuljangmassage": {"마곡동": "magok-dong", "화곡동": "hwagok-dong"},
    "nowon-gu-chuljangmassage": {"상계동": "sanggye-dong", "중계동": "junggye-dong"},
    "yangcheon-gu-chuljangmassage": {"목동": "mokdong"},
}


# 행정동 → 페이지 slug 링크 레지스트리.
# 기본값은 수기 작성 페이지(DONG_PAGES)이며, 자동 생성 모듈이
# register_dong_pages() 로 나머지 동을 병합한다(순환 import 방지).
_DONG_LINKS = {gu: dict(m) for gu, m in DONG_PAGES.items()}


def register_dong_pages(mapping):
    """자치구 slug → {동명: 페이지 slug} 매핑을 링크 레지스트리에 병합한다."""
    for gu_slug, dong_map in mapping.items():
        _DONG_LINKS.setdefault(gu_slug, {})
        for dong, slug in dong_map.items():
            # 수기 페이지가 우선(이미 등록된 동은 덮어쓰지 않음)
            _DONG_LINKS[gu_slug].setdefault(dong, slug)


def dong_nav_section(gu_slug, gu_name):
    """자치구 페이지에 들어갈 통합 행정동 안내 목록을 생성한다(ㄱㄴㄷ 정렬)."""
    dongs = DISTRICT_DONGS.get(gu_slug, [])
    if not dongs:
        return ""
    pages = _DONG_LINKS.get(gu_slug, {})
    items = []
    for d in sorted(dongs):
        if d in pages:
            items.append(f'<li><a href="{dong_url(pages[d])}">{d}</a></li>')
        else:
            items.append(f'<li><span>{d}</span></li>')
    return (
        f'<section class="district-dong-nav"><h2>{gu_name} 행정동 안내</h2>'
        f'<p>{gu_name}의 행정동을 ㄱㄴㄷ 순으로 정리했습니다. 1동·2동 등 번호로 나뉜 행정동은 대표 동 하나로 통합해 표시했으며, {gu_name} 전 행정동에 방문이 가능합니다. 각 동을 누르면 지역별 상세 안내를 확인하실 수 있습니다.</p>'
        f'<ul class="card-grid dong-nav-grid">{"".join(items)}</ul></section>'
    )


# 상단 메뉴
NAV = [
    ("홈", "/seoul-chuljangmassage/", []),
    ("출장마사지 안내", "/seoul-chuljangmassage/#service", [
        ("서비스 안내", "/seoul-chuljangmassage/#service"),
        ("전지역 방문 가능", "/seoul-chuljangmassage/#coverage"),
        ("예약 전 확인 기준", "/seoul-chuljangmassage/#check"),
        ("홈타이 이용 가이드", "/hometai-guide/"),
    ]),
    ("자치구별 안내", "/seoul-chuljangmassage/#districts", [
        (name, district_url(slug)) for slug, name in DISTRICTS
    ]),
    ("역세권별 안내", "/seoul-chuljangmassage/#stations", [
        (name, station_url(slug)) for slug, name in STATIONS_MENU
    ]),
    ("생활권별 안내", "/seoul-chuljangmassage/#zones", [
        (name, zone_url(slug)) for slug, name in ZONES
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 지역", "/reservation/#place"),
        ("결제·이동비 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
    ]),
    ("이용 전 확인사항", "/precautions/", [
        ("방문 전 준비", "/precautions/#prepare"),
        ("서울 교통·이동 기준", "/precautions/#outer"),
        ("위생·안전 기준", "/precautions/#hygiene"),
        ("자주 묻는 질문", "/precautions/#faq"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("개인정보처리방침", "/privacy/"),
    ]),
]
