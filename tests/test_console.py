#!/usr/bin/python3
"""Unittests for console.py"""

import os
import unittest
from models import storage
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    @classmethod
    def tearDownClass(self):
        try:
            os.remove("file.json")
        except IOError as e:
            pass

    def test_help_show(self):
        expected_output = "Display the string representation of an instance\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_EOF(self):
        expected_output = "Exit the program\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_create(self):
        expected_output = "Create a new instance of the specified \
class and save it\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_show(self):
        expected_output = "Display the string representation of an instance\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_destroy(self):
        expected_output = "Delete an instance from storage\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_all(self):
        expected_output = "Display string representations of all instances\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_update(self):
        expected_output = "Update an instance attribute \
and save changes to storage\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(f.getvalue(), expected_output)

    def test_help_count(self):
        expected_output = "Count the number of instances of a class\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(f.getvalue(), expected_output)

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual("** class name missing **\n",
                             f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(f.getvalue().strip()))
            testKey = "BaseModel.{}".format(f.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User 1234-absdd"))
            self.assertEqual("** no instance found **\n",
                             f.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User 123"))
            self.assertEqual("** no instance found **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 123"))
            self.assertEqual("** no instance found **\n",
                             f.getvalue())
            
    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertEqual("[]\n", f.getvalue())

    def test_update(self):
        """Test cmd output: update"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update User 1234-bcde"))
            self.assertEqual("** no instance found **\n",
                             f.getvalue())


if __name__ == '__main__':
    unittest.main()