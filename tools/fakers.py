from datetime import date, timedelta

from faker import Faker


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def date(self, start: timedelta = timedelta(days=-30), end: timedelta = timedelta()) -> date:
        return self.faker.date_between(start_date=start, end_date=end)

    def money(self, start: float = -100, end: float = 100) -> float:
        return self.faker.pyfloat(min_value=start, max_value=end)

    def category(self) -> str:
        return self.faker.random_element(['food', 'taxi', 'fuel', 'beauty', 'restaurants'])

    def sentence(self) -> str:
        return self.faker.sentence()


fake = Fake(faker=Faker())
