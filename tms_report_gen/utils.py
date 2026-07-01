import re

from pathlib import Path

from bs4 import BeautifulSoup


# Replace restricted characters in a filename
def sanitize_filename(name: str) -> str:

    name = re.sub(r'[\\/*?:"<>|]', "_", name)

    return name.strip()


# Write empty valuse as '-'
def format_value(value) -> str:

    if value is None:
        return "-"

    return str(value)


# Resolve image paths in HTML content to absolute file URIs based on the provided media root directory
def resolve_image_paths(
    html: str,
    media_root: str,
) -> str:

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    # Getting all the image tags and updating their src attributes to absolute file URIs
    for img in soup.find_all("img"):

        src = img.get("src")

        if not src:
            continue

        # Already resolved
        if src.startswith("file:///"):
            continue

        image_path = (
            Path(media_root) /
            src.lstrip("/")
        ).resolve()

        img["src"] = image_path.as_uri()

    return str(soup)