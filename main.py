import requests
import unittest
import logging

class PetStoreAPITests(unittest.TestCase):
    base_url = "https://petstore.swagger.io/v2"

    def setUp(self):
        logging.basicConfig(level=logging.INFO)

        file_handler = logging.FileHandler('test.log')
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(file_handler)

    def test_successful_request_returns_correct_http_status(self):
        response = requests.get(f"{self.base_url}/pet/1")
        self.assertEqual(response.status_code, 200)
        self.logger.info(f"Test 'test_successful_request_returns_correct_http_status' passed. HTTP status code: {response.status_code}")

    def test_successful_request_returns_correct_data_format(self):
        response = requests.get(f"{self.base_url}/pet/1")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.headers["Content-Type"].startswith("application/json"))
        self.logger.info("Test 'test_successful_request_returns_correct_data_format' passed. Correct data format")

    def test_invalid_parameters_return_correct_http_status(self):
        response = requests.get(f"{self.base_url}/pet/invalid_pet_id")
        self.assertEqual(response.status_code, 404)
        self.logger.info(f"Test 'test_invalid_parameters_return_correct_http_status' passed. HTTP status code: {response.status_code}")

    def test_invalid_parameters_return_correct_data_format(self):
        response = requests.get(f"{self.base_url}/pet/invalid_pet_id")
        self.assertEqual(response.status_code, 404)
        self.assertTrue(response.headers["Content-Type"].startswith("application/json"))
        self.logger.info("Test 'test_invalid_parameters_return_correct_data_format' passed. Correct data format for invalid parameters")

    def test_additional_test(self):
        self.logger.info("Test 'test_additional_test' passed.")

if __name__ == '__main__':
    unittest.main()
