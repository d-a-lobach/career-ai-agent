from urllib.parse import urlparse


def validate_hh_url(url: str) -> bool:

    try:
        parsed = urlparse(url)

        return (
            parsed.scheme in ("http", "https")
            and "hh.ru" in parsed.netloc
            and "/vacancy/" in parsed.path
        )

    except Exception:
        return False