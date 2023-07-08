from src.adapters.db import models
from src.business_logic.post import dto


def convert_post_model_to_dto(post: models.Post) -> dto.Post:
    return dto.Post(
        post_id=post.id,
        name=post.name
    )


def convert_post_models_to_dtos(posts: list[models.Post]) -> list[dto.Post]:
    list_posts = []
    for post in posts:
        list_posts.append(convert_post_model_to_dto(post=post))
    return list_posts