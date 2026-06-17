#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — Bing·Naver·Yandex·Seznam 공통(인증 키 불필요).

IndexNow 는 한 곳(api.indexnow.org)에 통보하면 참여 검색엔진 전체에 전파된다.
네이버·빙·얀덱스가 참여하므로 글을 올리거나 수정할 때마다 즉시 색인 요청이 된다.
(구글은 IndexNow 미참여 — tools/google_indexing.py 또는 서치콘솔 사용)

사용법:
  python tools/indexnow.py                # sitemap.xml 의 모든 URL 제출
  python tools/indexnow.py --changed      # 직전 커밋에서 바뀐 페이지만 제출(CI용)
  python tools/indexnow.py URL1 URL2 ...  # 지정한 URL만 제출
"""
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = BASE.split("://", 1)[-1]
ENDPOINT = "https://api.indexnow.org/indexnow"


def _path_to_url(path):
    """'seoul/foo/index.html' → BASE/seoul/foo/ , 'index.html' → BASE/"""
    p = path[:-len("index.html")] if path.endswith("index.html") else path
    p = p.lstrip("./")
    return f"{BASE}/{p}"


def sitemap_urls():
    xml = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def changed_urls():
    """직전 커밋(HEAD~1..HEAD)에서 추가·수정된 index.html → URL 목록."""
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", "--diff-filter=AM", "HEAD~1", "HEAD"],
            cwd=ROOT, text=True,
        )
    except subprocess.CalledProcessError:
        return []
    urls = [_path_to_url(f) for f in out.split() if f.endswith("index.html")]
    return sorted(set(urls))


def submit(urls):
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow {r.status} {r.reason} — {len(urls)} URL 제출")


def main():
    args = sys.argv[1:]
    if args == ["--changed"]:
        urls = changed_urls() or sitemap_urls()
    elif args:
        urls = args
    else:
        urls = sitemap_urls()
    if not urls:
        print("제출할 URL이 없습니다.")
        return
    # IndexNow 1회 최대 10,000 URL
    for i in range(0, len(urls), 10000):
        submit(urls[i:i + 10000])


if __name__ == "__main__":
    main()
