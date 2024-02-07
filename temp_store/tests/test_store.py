
from unittest.mock import MagicMock
from unittest import TestCase, main
from temp_store.store import TemperatureStore, TemperatureRetriever

class Tests(TestCase):
	
	def test_store_and_retrieve(self):
		# 1 set up
		store = TemperatureStore()
		lat, long = 60.36926,5.34975
		ts = "2024-01-31T12:31:55"
		# 2 calling the unit under test
		store.store(lat, long, ts, 5.2)
		val = store.retrieve(lat, long, ts)
		# 3 assert
		self.assertEqual(5.2, val)

	def test_retrieve_non_existent(self):
		store = TemperatureStore()
		lat, long = 60.36926,5.34975
		ts = "2024-01-31T12:31:55"
		val = store.retrieve(lat, long, ts)
		self.assertIsNone(val)


	#Integration test (not anymore because Mock is used)
	def test_web_retriever_into_store(self):
		retr = TemperatureRetriever()
		retr.retrieve = MagicMock(return_value=23)
		store = TemperatureStore()

		lat, long = 60.36926,5.34975
		ts = "2024-01-31T12:31:55"
		data = retr.retrieve(lat, long, ts)
		store.store(lat, long, ts, data)
		
		val = store.retrieve(lat, long, ts)
		self.assertEqual(23, val)
		#...

if __name__ == '__main__':
	main()


