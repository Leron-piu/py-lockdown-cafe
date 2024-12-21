from app.errors import VaccineError, NotWearingMaskError, NotVaccinatedError, OutdatedVaccineError
from app.cafe import Cafe


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
        raise NotWearingMaskError(f"Friends should buy {mask_count} masks")
    print(f"Friends can go to {cafe.name}")
