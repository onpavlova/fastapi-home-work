
from pydantic import BaseModel, validator #, EmailStr


class Good(BaseModel):
    title: str
    weight: int
    description: str | None = None
    article: str | None
    new_super: str | None = None


    @validator("weight")
    def check_year(cls, value):
        """
        Проверка корректности ввода значения года.
        :type value: object
        """
        if value < 0:
            raise ValueError("Введите корректный вес")
        return value




    #
    # @validator("date_to")
    # def check_date_to(cls, value):
    #     """
    #     Проверка корректности ввода значения срока годности.
    #     :type value: object
    #     """
    #     current_datetime = datetime.now()
    #
    #     if value < current_datetime:
    #         raise ValueError("Товар просрочен")
    #     return value

#class MovieId(Movie):
#    movie_id: int

#class MovieEmail(Movie):
#    email: EmailStr
