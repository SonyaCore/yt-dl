import re
from config import YOUTUBE_LINK_REGEX


def link_is_valid(video_link: str) -> bool:
    """
    validation youtube video link

    params : link : link for validate

    return : True if link is valid
    """

    if "youtube" not in video_link or len(re.findall(YOUTUBE_LINK_REGEX, video_link)) < 1:
        return False
    else:
        return True
