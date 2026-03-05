def quality_check(content_dict):
    reviewed = {}
    for platform, text in content_dict.items():
        lines = text.split("\n")
        unique_lines = list(dict.fromkeys(lines))
        reviewed[platform] = "\n".join(unique_lines)
    return reviewed