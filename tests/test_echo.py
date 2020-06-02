#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):
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

        self.assertEqual(stdout, usage)

    def test_upper(self):
        """Running the program with -u --upper
        should change statement to uppercase"""
        p = echo.create_parser()
        test_args = ['Hello world', '-u']
        ns = p.parse_args(test_args)
        self.assertTrue(ns.statement == 'Hello world')
        self.assertTrue(ns.u, 'Parser does not accept -u')

        # Run the command 'python echo.py -u Hello world' in a separte process,
        # collect output and check if it matches 'HELLO WORLD'
        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "Hello world"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(stdout, 'HELLO WORLD')

    def test_lower(self):
        """Running the program with -l --lower
        should change statement to lowercase"""
        p = echo.create_parser()
        test_args = ['Hello world', '-l']
        ns = p.parse_args(test_args)
        self.assertTrue(ns.statement == 'Hello world')
        self.assertTrue(ns.l, 'Parser does not accept -l')

        # Run the command 'python echo.py -l Hello world' in a separte process,
        # collect output and check if it matches 'hello world'
        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "Hello world"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(stdout, 'hello world')

    def test_title(self):
        """Running the program with -t --title
        should change statement to init cap"""
        p = echo.create_parser()
        test_args = ['hello world', '-t']
        ns = p.parse_args(test_args)
        self.assertTrue(ns.statement == 'hello world')
        self.assertTrue(ns.t, 'Parser does not accept -t')

        # Run the command 'python echo.py -t hello world' in a separte process,
        # collect output and check if it matches 'Hello World'
        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello world"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(stdout, 'Hello World')

    def test_multiple_args(self):
        """Running the program with -tul
        should change statement to lowercase"""

        # Run the command 'python echo.py -t hello world' in a separte process,
        # collect output and check if it matches 'Hello World'
        process = subprocess.Popen(
            ["python", "./echo.py", "-tul", "heLLo woRLd"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(stdout, 'hello world')
    
    def test_statement_only(self):
        """Running the program with only statement
        should print statement"""

        # Run the command 'python echo.py -t hello world' in a separte process,
        # collect output and check if it matches 'Hello World'
        process = subprocess.Popen(
            ["python", "./echo.py", "heLLo woRLd"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEqual(stdout, 'heLLo woRLd')

    pass


if __name__ == '__main__':
    unittest.main()
