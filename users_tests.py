import unittest
from unittest.mock import AsyncMock, patch
from users import UserDTO, UserService


class TestUserService(unittest.TestCase):

    @patch("users.AsyncSession")
    async def test_get_existing_user(self, mock_session):
        # Arrange
        user_id = 1
        mock_session_instance = AsyncMock()
        expected_user = UserDTO(id=user_id, name="First")
        mock_session_instance.get.return_value = expected_user
        mock_session.return_value.__aenter__.return_value = mock_session_instance

        user_service = UserService(mock_session)

        # Act
        result = await user_service.get(user_id)

        # Assert
        self.assertEqual(result, expected_user)
        mock_session.assert_called_once()
        mock_session_instance.get.assert_called_once_with(UserDTO, user_id)

    @patch("users.AsyncSession")
    async def test_get_nonexistent_user(self, mock_session):
        # Arrange
        user_id = 2
        mock_session_instance = AsyncMock()
        mock_session_instance.get.return_value = None
        mock_session.return_value.__aenter__.return_value = mock_session_instance

        user_service = UserService(mock_session)

        # Act
        result = await user_service.get(user_id)

        # Assert
        self.assertIsNone(result)
        mock_session.assert_called_once()
        mock_session_instance.get.assert_called_once_with(UserDTO, user_id)

    @patch("users.AsyncSession")
    async def test_get_error_handling(self, mock_session):
        # Arrange
        user_id = 3
        mock_session_instance = AsyncMock()
        mock_session_instance.get.side_effect = Exception("Database error")
        mock_session.return_value.__aenter__.return_value = mock_session_instance

        user_service = UserService(mock_session)

        # Act and Assert
        with self.assertRaises(ValueError):
            await user_service.get(user_id)
        mock_session.assert_called_once()
        mock_session_instance.get.assert_called_once_with(UserDTO, user_id)

    @patch("users.AsyncSession")
    async def test_add_user(self, mock_session):
        # Arrange
        user = UserDTO(id=4, name="Second")
        mock_session_instance = AsyncMock()
        mock_session.return_value.__aenter__.return_value = mock_session_instance

        user_service = UserService(mock_session)

        # Act
        await user_service.add(user)

        # Assert
        mock_session.assert_called_once()
        mock_session_instance.add.assert_called_once_with(user)
        mock_session_instance.commit.assert_called_once()

    @patch("users.AsyncSession")
    async def test_add_user_error_handling(self, mock_session):
        # Arrange
        user = UserDTO(id=5, name="First")
        mock_session_instance = AsyncMock()
        mock_session_instance.add.side_effect = Exception("Database error")
        mock_session.return_value.__aenter__.return_value = mock_session_instance

        user_service = UserService(mock_session)

        # Act and Assert
        with self.assertRaises(ValueError):
            await user_service.add(user)
        mock_session.assert_called_once()
        mock_session_instance.add.assert_called_once_with(user)
        mock_session_instance.commit.assert_not_called()


if __name__ == "__main__":
    unittest.main()
