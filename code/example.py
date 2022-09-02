# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License

# Very simple script to demonstrate run in environment
# Print message passed in as environment variable
import os
import pip_install_test
from mycode1.main import *

# print(os.environ.get("MESSAGE"))
print("I am in the environment!")
train()
