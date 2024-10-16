# Example function which interacts with an external service
class ExternalService:
    def fetch_data(self):
        return "real data"

def process_data(service):
    data = service.fetch_data()
    return f"Processed {data}"

# Unit test using Mock Object pattern
import unittest
from unittest.mock import MagicMock

class TestDataService(unittest.TestCase):
    def test_process_data(self):
        # Arrange
        mock_service = MagicMock()
        mock_service.fetch_data.return_value = "mock data"
        expected = "Processed mock data"

        # Act
        result = process_data(mock_service)

        # Assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
