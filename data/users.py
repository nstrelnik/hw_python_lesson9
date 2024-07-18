import dataclasses

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth_day: str
    date_of_birth_month: str
    date_of_birth_year: str
    subjects: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str
