from __future__ import annotations
from app.errors import VaccineError, NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError
from app.cafe import Cafe
import datetime


def go_to_cafe(friends: list, cafe: Cafe):
    mask_count = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            raise
        except NotWearingMaskError:
            mask_count += 1
    if mask_count != 0:
        print(f"Friends should buy {mask_count} masks")
        raise NotVaccinatedError
    print(f"Friends can go to {cafe.name}")
