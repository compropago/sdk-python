from compropago.factory.models.instructiondetails import InstructionDetails


class Instructions:
    description = None
    step_1 = None
    step_2 = None
    step_3 = None
    note_extra_comition = None
    note_expiration_date = None
    note_confirmation = None
    details = None

    def __init__(self):
        self.details = InstructionDetails()
