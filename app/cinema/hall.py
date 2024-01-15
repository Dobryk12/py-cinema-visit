from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
class CinemaHall:
    def __init__(self, number):
        self.number= number

    def movie_session(self, movie_name: str, customers: list[Customer], cleaner_stuff: Cleaner):
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.whatch_movie(movie_name)
        print(f'"{movie_name}" ended.')

        cleaner_stuff.clean_hall(self.number)