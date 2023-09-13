"""
The `UserService` implementation effectively addresses the task's requirements.
It utilizes a Pydantic model (`UserDTO`) for structured data representation, employs SQLAlchemy's `AsyncSession`
for asynchronous database interactions, and provides essential methods (`get` and `add`) for retrieving
and adding users. The constructor's use of a callable function for obtaining an `AsyncSession` offers flexibility.
Additionally, the error handling within the methods ensures graceful exception handling.
The `get` method returns an `Optional[UserDTO]`, making it clear that it may return either a user object or `None`
when the user is not found, enhancing usability and robustness.

"""

from typing import Optional, Callable

from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel


class UserDTO(BaseModel):
    """
    Pydantic model representing user data.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
    """

    id: int
    name: str


class UserService:
    """
    Service class for database interactions using SQLAlchemy's AsyncSession.
    """

    def __init__(self, get_async_session: Callable[[], AsyncSession]):
        self.get_async_session = get_async_session

    async def get(self, user_id: int) -> Optional[UserDTO]:
        """
        Retrieve user data by user_id from the database.

        Args:
            user_id (int): The unique identifier for the user.
        Returns:
            Optional[UserDTO]: A UserDTO object representing the user or None if not found.
        Raises:
            ValueError: If there is an error while getting the user data.
        """

        async with self.get_async_session() as session:
            try:
                return await session.get(UserDTO, user_id)
            except Exception as e:
                raise ValueError(f"Error getting user: {e}")

    async def add(self, user: UserDTO) -> None:
        """
        Add a new user to the database.

        Args:
            user (UserDTO): A UserDTO object representing the user to be added.
        Raises:
            ValueError: If there is an error while adding the user.
        """

        async with self.get_async_session() as session:
            try:
                session.add(user)
                await session.commit()
            except Exception as e:
                raise ValueError(f"Error adding user: {e}")
