from abc import ABC, abstractmethod


class ImagesRepository(ABC):
    @abstractmethod
    def upload_object(self, base64_image: str, filepath: str) -> str:
        pass