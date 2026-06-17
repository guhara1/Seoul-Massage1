# 색인 인덱싱 도구 안내

서울 출장마사지 사이트의 빠른 색인을 위한 파일·스크립트 모음입니다.

## 자동 생성되는 색인 파일 (build.py 실행 시)

| 파일 | 용도 |
|---|---|
| `sitemap.xml` | 색인 대상 전체 URL + `lastmod`. 구글·네이버·빙 공통 |
| `rss.xml` | RSS 2.0 피드(피드 기반 색인 발견). 모든 페이지에 자동발견 링크 포함 |
| `robots.txt` | 구글·네이버(Yeti)·빙 허용 + `Sitemap` 2줄(sitemap, rss) |
| `<INDEXNOW_KEY>.txt` | IndexNow 인증 키 파일(루트 게시). 키는 `content/site.py`의 `INDEXNOW_KEY` |

## 1. IndexNow — Bing·Naver·Yandex 즉시 통보 (권장, 인증 불필요)

IndexNow 는 한 번 통보하면 참여 검색엔진 전체에 전파됩니다. **네이버·빙·얀덱스**가
참여하므로 글을 올리거나 수정할 때 즉시 색인 요청이 됩니다.

```bash
python tools/indexnow.py            # sitemap 전체 제출
python tools/indexnow.py --changed  # 직전 커밋에서 바뀐 페이지만 (CI용)
python tools/indexnow.py https://seoul-massage1.pages.dev/seoul/...   # 지정 URL
```

- **자동화**: `.github/workflows/indexnow.yml` 가 `main` 푸시(배포)마다 바뀐 URL을
  자동 제출합니다. 별도 시크릿이 필요 없습니다.

## 2. 구글 — IndexNow 미참여

구글은 IndexNow에 참여하지 않습니다. 구글의 정석은 **Search Console 사이트맵 제출**입니다.

1. [Google Search Console](https://search.google.com/search-console) 속성 등록(도메인/URL 접두어)
2. 소유확인(이미 메인 `<head>`에 네이버 인증 메타 있음 / 구글은 HTML 태그·파일 방식 선택)
3. 사이트맵 메뉴에 `sitemap.xml` 제출

### (선택) 구글 Indexing API
> ⚠️ 공식적으로 JobPosting·BroadcastEvent 유형만 지원합니다. 일반 페이지는 보장되지
> 않으므로 보조 수단입니다.

```bash
pip install google-auth
GOOGLE_APPLICATION_CREDENTIALS=service.json python tools/google_indexing.py
```

CI 자동화: 저장소 **Variables** 에 `ENABLE_GOOGLE_INDEXING=true`, **Secrets** 에
`GOOGLE_INDEXING_CREDENTIALS`(서비스계정 JSON 원문)를 등록하면 워크플로가 함께 돕니다.

## 3. 네이버 서치어드바이저

1. [네이버 서치어드바이저](https://searchadvisor.naver.com) 사이트 등록
2. 소유확인 — 메인 `<head>`의 `naver-site-verification` 메타로 확인
3. 사이트맵 제출: `https://seoul-massage1.pages.dev/sitemap.xml`
4. RSS 제출: `https://seoul-massage1.pages.dev/rss.xml`
5. 네이버는 IndexNow 참여사이므로 `tools/indexnow.py` 로도 즉시 통보됩니다.

## 참고 — 사이트맵 핑(ping)은 더 이상 동작하지 않습니다

구글(`/ping?sitemap=`, 2023년 중단)과 빙 모두 사이트맵 핑 엔드포인트를 폐지했습니다.
따라서 "핑" 대신 **IndexNow(빙·네이버) + Search Console 사이트맵 제출(구글)** 조합이
현재 가장 빠른 색인 방법입니다.
