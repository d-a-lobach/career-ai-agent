import re


def normalize_spaces(text: str) -> str:

    text = re.sub(
        r"[ \t]+",
        " ",
        text,
    )

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text,
    )

    return text.strip()


def truncate(
    text: str,
    max_length: int,
) -> str:

    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."