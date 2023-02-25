class Book:
    def __init__(
            self,
            name: str,
            description: str,
            price: int,
            list_count: int,
            rate_list: list[int]
        ) -> None:
            self.name = name
            self.description = description
            self.price = price
            self.list_count = list_count
            self.rate_list = rate_list

    @property
    def rate(self) -> float:
          return sum(self.rate_list) / len(self.rate_list)