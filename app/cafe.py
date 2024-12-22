from app.errors import (NotVaccinatedError, NotWearingMaskError,
                        OutdatedVaccineError)
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("All friends should be vaccinated")
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("All friends should be vaccinated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"
