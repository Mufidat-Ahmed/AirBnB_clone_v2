import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

		def test_do_create_valid_args(self):
				hbnb_command = HBNBCommand()
				args = ["State", "name=Atlanta"]
				result = hbnb_command.do_create(args)

				self.assertEqual(result, None)
				self.assertIn("Atlanta", hbnb_command.storage.all())

		def test_do_create_invalid_class_name(self):
				hbnb_command = HBNBCommand()
				args = ["InvalidClass", "name=Atlanta"]
				with self.assertRaises(Exception):
						hbnb_command.do_create(args)

		def test_do_show_valid_args(self):
				hbnb_command = HBNBCommand()
				hbnb_command.do_create(["State", "name=Atlanta"])

				args = ["State", "Atlanta"]
				result = hbnb_command.do_show(args)

				self.assertEqual(result, None)
				self.assertIn("Atlanta", result)

		def test_do_show_invalid_class_name(self):
				hbnb_command = HBNBCommand()

				args = ["InvalidClass", "Atlanta"]
				with self.assertRaises(Exception):
						hbnb_command.do_show(args)

		def test_do_destroy_valid_args(self):
				hbnb_command = HBNBCommand()
				hbnb_command.do_create(["State", "name=Atlanta"])

				args = ["State", "Atlanta"]
				result = hbnb_command.do_destroy(args)

				self.assertEqual(result, None)
				self.assertNotIn("Atlanta", hbnb_command.storage.all())

		def test_do_destroy_invalid_class_name(self):
				hbnb_command = HBNBCommand()

				args = ["InvalidClass", "Atlanta"]
				with self.assertRaises(Exception):
						hbnb_command.do_destroy(args)

		def test_do_all_valid_args(self):
				hbnb_command = HBNBCommand()
				hbnb_command.do_create(["State", "name=Atlanta"])
				hbnb_command.do_create(["State", "name=Arizona"])

				args = []
				result = hbnb_command.do_all(args)

				self.assertEqual(result, None)
				self.assertIn("Atlanta", result)
				self.assertIn("Arizona", result)

		def test_do_all_invalid_class_name(self):
				hbnb_command = HBNBCommand()

				args = ["InvalidClass"]
				with self.assertRaises(Exception):
						hbnb_command.do_all(args)

		def test_do_count_valid_args(self):
				hbnb_command = HBNBCommand()
				hbnb_command.do_create(["State", "name=Atlanta"])
				hbnb_command.do_create(["State", "name=Arizona"])

				args = ["State"]
				result = hbnb_command.do_count(args)

				self.assertEqual(result, 2)

		def test_do_count_invalid_class_name(self):
				hbnb_command = HBNBCommand()

				args = ["InvalidClass"]
				with self.assertRaises(Exception):
						hbnb_command.do_count(args)

		def test_do_update_valid_args(self):
				hbnb_command = HBNBCommand()
				hbnb_command.do_create(["State", "name=Atlanta"])

				args = ["State", "Atlanta", "name=Atlanta 2"]
				result = hbnb_command.do_update(args)

				self.assertEqual(result, None)
				self.assertEqual(hbnb_command.storage.all()["State.Atlanta"].name, "Atlanta 2")

		def test_do_update_invalid_class_name(self):
				hbnb_command = HBNBCommand()

				args = ["InvalidClass", "Atlanta", "name=Atlanta 2"]
				with self.assertRaises(Exception):
						hbnb_command.do_update(args)


if __name__ == "__main__":
		unittest.main()
