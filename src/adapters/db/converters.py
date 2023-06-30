from src.adapters.db import models
from src.business_logic.post import dto


def convert_post_model_to_dto(post: models.Post) -> dto.Post:
    return dto.Post(
        post_id=post.id,
        name=post.name
    )
