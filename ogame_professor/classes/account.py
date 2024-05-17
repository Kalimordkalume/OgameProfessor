from database import data

class Account:
    """This class will represent the structure of the player account."""

    def __init__(self) -> None:
        self.planet_list: list = None
        self.technologies_list: list = None
        self.account_class: str = None
        self.is_commander: bool = None
        self.is_engineer: bool = None
        self.is_technocrat: bool = None
        self.is_geologist: bool = None
        self.is_admiral: bool = None

    def gather_account_data(self):
        ...

    
