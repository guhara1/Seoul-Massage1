#!/usr/bin/env python3
"""Google Indexing API 제출 (구글용 — IndexNow 미참여 대안).

⚠️ 주의: 구글 Indexing API 는 공식적으로 JobPosting·BroadcastEvent 유형만
지원합니다. 일반 페이지도 호출은 되지만 색인이 보장되지는 않습니다.
일반 페이지는 Search Console 사이트맵 제출이 정석이며, 본 스크립트는 보조용입니다.

준비:
  1) Google Cloud 콘솔에서 'Indexing API' 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Search Console 속성 설정 → 사용자/권한에 서비스 계정 이메일을 '소유자'로 추가
  4) pip install google-auth

사용법:
  GOOGLE_APPLICATION_CREDENTIALS=service.json \
      python tools/google_indexing.py                 # sitemap.xml 전체
  GOOGLE_APPLICATION_CREDENTIALS=service.json \
      python tools/google_indexing.py URL1 URL2 ...    # 지정 URL
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls():
    xml = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def session():
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성 필요: pip install google-auth")
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스계정 JSON 경로를 지정하세요.")
    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    return AuthorizedSession(creds)


def main():
    urls = sys.argv[1:] or sitemap_urls()
    if not urls:
        print("제출할 URL이 없습니다.")
        return
    s = session()
    ok = 0
    for u in urls:
        body = {"url": u, "type": "URL_UPDATED"}
        r = s.post(ENDPOINT, json=body)
        if r.status_code == 200:
            ok += 1
        else:
            print(f"  실패 {r.status_code}: {u} — {r.text[:120]}")
    print(f"Google Indexing API: {ok}/{len(urls)} 성공")


if __name__ == "__main__":
    main()
