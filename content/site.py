# 사이트 공통 설정
BASE_URL = "https://www.ganda-go.example.com"

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
