from typing import List

PLATFORM_TONES = {
    "linkedin": "professional, thoughtful, brief",
    "twitter": "concise, engaging thread",
    "youtube": "explanatory video script style",
    "newsletter": "digest, structured format"
}

def create_generation_plan(key_sentences: List[str], platforms: List[str]):
    plan = {}
    for platform in platforms:
        plan[platform] = {
            "tone": PLATFORM_TONES.get(platform, "neutral"),
            "content": key_sentences
        }
    return plan