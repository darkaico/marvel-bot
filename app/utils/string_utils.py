def limit_text(text_to_limit: str, limit: int = 200):
    limit = limit - 3

    return (text_to_limit[:limit] + "...") if len(text_to_limit) > limit else text_to_limit


def remove_params(url: str):
    return url.split("?")[0]
