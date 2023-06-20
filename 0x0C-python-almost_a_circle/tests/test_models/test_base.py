#!/usr/bin/python3
"""This is a test suite for the models/base.py file
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ A series of tests"""
    def setUp(self):
        """Setup some general items"""
        self.base_instance = Base()

    def tearDown(self):
        """Unset them"""
        self.base_instance = None

    def test_instance_creation(self):
        """test instance creation"""
        self.assertIsInstance(self.base_instance, Base)

    def test_id_generation(self):
        """Check id gen"""
        self.assertNotEqual(self.base_instance.id, 1)

    def test_id_customization(self):
        """ Test that the id attribute is set correctly when id is provided"""
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_id_type(self):
        """ Test that the id attribute is of type int"""
        base = Base()
        self.assertIsInstance(base.id, int)

    def test_id_increment(self):
        """ Test that the id attribute increments correctly"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)

    def test_id_uniqueness(self):
        """ Test that each instance has a unique id"""
        base1 = Base()
        base2 = Base()
        self.assertNotEqual(base1.id, base2.id)

    def test_id_uniqueness(self):
        """ Test that each instance has a unique id"""
        base1 = Base()
        base2 = Base()
        self.assertNotEqual(base1.id, base2.id)

    def test_id_float(self):
        """Test that providing a float id sets the id attribute as an integer"""
        base = Base(3.14)
        self.assertNotEqual(base.id, 3)

    def test_id_inheritance(self):
        """Test that the id attribute is accessible in subclasses"""
        class Derived(Base):
            pass
        derived = Derived()
        self.assertTrue(hasattr(derived, 'id'))

    def test_load_from_file_method(self):
        """ Test the load_from_file method """
        rect1 = Rectangle(5, 10)
        rect2 = Rectangle(7, 3)
        Rectangle.save_to_file([rect1, rect2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertIsInstance(loaded_rectangles[1], Rectangle)


class TestToJsonString(unittest.TestCase):
    """Testcase"""
    def test_empty_list(self):
        """ Test with an empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, [])

    def test_single_dictionary(self):
        """ Test with a single dictionary"""
        dictionary = {'id': 1, 'name': 'John'}
        result = Base.to_json_string([dictionary])
        expected_output = json.dumps([dictionary])
        self.assertEqual(result, expected_output)

    def test_multiple_dictionaries(self):
        """ Test with multiple dictionaries"""
        dictionaries = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}, {'id': 3, 'name': 'Alice'}]
        result = Base.to_json_string(dictionaries)
        expected_output = json.dumps(dictionaries)
        self.assertEqual(result, expected_output)

    def test_none_input(self):
        """ Test with None input"""
        result = Base.to_json_string(None)
        self.assertEqual(result, [])

    def test_invalid_input(self):
        """ Test with invalid input"""
        result = Base.to_json_string('invalid')
        self.assertEqual(result, '"invalid"')

    def test_nested_dictionaries(self):
        """ Test with nested dictionaries"""
        dictionaries = [{'id': 1, 'name': 'John', 'address': {'street': 'Main St', 'city': 'New York'}}]
        result = Base.to_json_string(dictionaries)
        expected_output = json.dumps(dictionaries)
        self.assertEqual(result, expected_output)

    def test_unicode_characters(self):
        """ Test with unicode characters"""
        dictionaries = [{'id': 1, 'name': 'Héllo'}, {'id': 2, 'name': 'Wørld'}]
        result = Base.to_json_string(dictionaries)
        expected_output = json.dumps(dictionaries)
        self.assertEqual(result, expected_output)

    def test_empty_string(self):
        """ Test with an empty string"""
        result = Base.to_json_string('')
        self.assertEqual(result, [])

    def test_numeric_values(self):
        """ Test with numeric values"""
        dictionaries = [{'id': 1, 'value': 10.5}, {'id': 2, 'value': -5}]
        result = Base.to_json_string(dictionaries)
        expected_output = json.dumps(dictionaries)
        self.assertEqual(result, expected_output)

    def test_boolean_values(self):
        """ Test with boolean values"""
        dictionaries = [{'id': 1, 'flag': True}, {'id': 2, 'flag': False}]
        result = Base.to_json_string(dictionaries)
        expected_output = json.dumps(dictionaries)
        self.assertEqual(result, expected_output)

    def test_mixed_data_types(self):
        """ Test with mixed data types"""
        dictionaries = [{'id': 1, 'name': 'John', 'age': 25, 'is_student': True},
                        {'id': 2, 'name': 'Jane', 'age': 30, 'is_student': False}]
        result = Base.to_json_string(dictionaries)
        expected_output = json.dumps(dictionaries)
        self.assertEqual(result, expected_output)


class TestSaveToFile(unittest.TestCase):
    """Testcase"""
    def setUp(self):
        self.base_instance = Base()

    def tearDown(self):
        del self.base_instance

    def test_save_empty_list(self):
        """ Test saving an empty list"""
        filename = "EmptyList.json"
        save_to_file(Base, [])
        with open(filename, 'r') as file:
            content = file.read()
        self.assertEqual(content, '[]')
        """ Clean up the created file"""
        self.remove_file(filename)

    def test_save_single_instance(self):
        """ Test saving a single instance"""
        filename = "SingleInstance.json"
        instance = self.base_instance
        save_to_file(Base, [instance])
        with open(filename, 'r') as file:
            content = file.read()
        expected_output = '[{"id": 1}]'
        self.assertEqual(content, expected_output)
        """ Clean up the created file"""
        self.remove_file(filename)

    def test_save_multiple_instances(self):
        """ Test saving multiple instances"""
        filename = "MultipleInstances.json"
        instances = [Base(), Base(), Base()]
        save_to_file(Base, instances)
        with open(filename, 'r') as file:
            content = file.read()
        expected_output = '[{"id": 1}, {"id": 2}, {"id": 3}]'
        self.assertEqual(content, expected_output)
        """ Clean up the created file"""
        self.remove_file(filename)

    def test_save_none_input(self):
        """ Test saving None input"""
        filename = "NoneInput.json"
        save_to_file(Base, None)
        with open(filename, 'r') as file:
            content = file.read()
        self.assertEqual(content, '[]')
        """ Clean up the created file"""
        self.remove_file(filename)

    def test_save_invalid_input(self):
        """ Test saving invalid input"""
        filename = "InvalidInput.json"
        save_to_file(Base, 'invalid')
        with open(filename, 'r') as file:
            content = file.read()
        self.assertEqual(content, '[]')
        """ Clean up the created file"""
        self.remove_file(filename)

    def remove_file(self, filename):
        """ Helper method to remove the created file"""
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
