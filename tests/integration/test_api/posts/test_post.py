import pytest


class TestPostControllers:
    @pytest.mark.asyncio
    async def test_posts_get(self, integration_client):
        response = await integration_client.get("posts/")

        assert response.status_code == 200
        assert response.json() == []

    @pytest.mark.asyncio
    async def test_get_posts_from_db(
            self,
            integration_client,
            post_data,
            create_posts_in_db
    ):
        await create_posts_in_db(**post_data)

        response = await integration_client.get("posts/")

        assert response.status_code == 200
        assert len(response.json()) == 1

        data = response.json()
        print(data)

        assert data[0]["post_id"] == post_data["post_id"]
        assert data[0]["name"] == post_data["post_name"]
