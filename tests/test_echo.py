#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):
    def setUp(self):
        super(TestEcho, self).setUp()
        self.addTypeEqualityFunc(str, self.assertMultiLineEqual)

    def test_help(self):
        """Running the program without arguments should show usage."""

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect its output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        with open("USAGE") as f:
            usage = f.read()

        self.assertEqual(stdout.decode('utf-8'), usage)

    def test_upper(self):
        """Running the program with -u --upper
        should change statement to uppercase"""
        p = echo.create_parser()
        test_args = ['Hello world', '-u']
        ns = p.parse_args(test_args)
        self.assertTrue(ns.text == 'Hello world')
        self.assertTrue(ns.upper, 'Parser does not accept -u')

        # output = echo.text_upper("Hello world")
        # Run the command 'python echo.py -u Hello world' in a separte process,
        # collect output and check if it matches 'HELLO WORLD'
        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "Hello world"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertTrue(stdout.isupper())

    def test_lower(self):
        """Running the program with -l --lower
        should change statement to lowercase"""
        p = echo.create_parser()
        test_args = ['Hello world', '-l']
        ns = p.parse_args(test_args)
        self.assertTrue(ns.text == 'Hello world')
        self.assertTrue(ns.lower, 'Parser does not accept -l')

        # Run the command 'python echo.py -l Hello world' in a separte process,
        # collect output and check if it matches 'hello world'
        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "Hello world"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(stdout.decode('utf-8'), 'hello world\n')

    def test_title(self):
        """Running the program with -t --title
        should change statement to init cap"""
        p = echo.create_parser()
        test_args = ['hello world', '-t']
        ns = p.parse_args(test_args)
        self.assertTrue(ns.text == 'hello world')
        self.assertTrue(ns.title, 'Parser does not accept -t')

        # Run the command 'python echo.py -t hello world' in a separte process,
        # collect output and check if it matches 'Hello World'
        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello world"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(stdout.decode('utf-8'), 'Hello World\n')

    def test_multiple_args(self):
        """Running the program with -ult
        should change statement to lowercase"""

        # Run the command 'python echo.py -t hello world' in a separte process,
        # collect output and check if it matches 'Hello World'
        process = subprocess.Popen(
            ["python", "./echo.py", "-ult", "heLLo woRLd"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(stdout.decode('utf-8'), 'Hello World\n')

    def test_statement_only(self):
        """Running the program with only text
        should print text"""

        # Run the command 'python echo.py -t hello world' in a separte process,
        # collect output and check if it matches 'Hello World'
        process = subprocess.Popen(
            ["python", "./echo.py", "heLLo woRLd"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(stdout.decode('utf-8'), 'heLLo woRLd\n')

    pass


if __name__ == '__main__':
    unittest.main()
