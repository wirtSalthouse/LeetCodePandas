#!/bin/bash

mkdir $1
PROGRAM="$1"/"$1.py"
TESTS="$1"/"$1_tests.py"

#create files with naming
touch "$1/README.md"
touch "$PROGRAM"
touch "$TESTS"

#populate with boilerplate stubs

printf "import pandas as pd\n\n" >> "$PROGRAM"
echo '# define function here:'>>"$PROGRAM"

printf "import unittest\n" >> "$TESTS"
printf "import pandas as pd\n" >> "$TESTS"
printf "from TestUtils.testUtils import is_equal_dataframes\n\n\n" >> "$TESTS"
printf "# remember to import the function to test\n\n" >> "$TESTS"
printf "class %sTests(unittest.TestCase):\n" "$1" >> "$TESTS"
printf "\tdef test_something(self):\n" >> "$TESTS"
printf "\t\tself.assertEqual(True, False)\n\n" >> "$TESTS"
printf "if __name__ == '__main__':\n">> "$TESTS"
printf "\tunittest.main()" >> "$TESTS"

