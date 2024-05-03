from uuid import UUID


class UserModel:
    def __init__(
        self,
        id: UUID,
        name: str | None,
        last_name: str | None,
        email: str | None,
        profile_image: str | None,
    ):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.profile_image = profile_image
