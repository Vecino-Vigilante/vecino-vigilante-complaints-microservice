from uuid import UUID


class MarkerModel:
    def __init__(
        self,
        marker_id: UUID,
        incident_id: UUID,
        direction: str,
        latitude: float,
        longitude: float      
    ) -> None:
        self.marker_id = marker_id
        self.incident_id = incident_id
        self.direction = direction
        self.latitude = latitude
        self.longitude = longitude