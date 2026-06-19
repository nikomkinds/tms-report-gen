import re


# Replace restricted characters in a filename
def sanitize_filename(name: str) -> str:

    name = re.sub(r'[\\/*?:"<>|]', "_", name)

    return name.strip()