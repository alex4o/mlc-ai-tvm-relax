# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""The ir module parser"""
from tvm.ir import Range
from ...ir_builder.ir import *  # pylint: disable=redefined-builtin
from . import parser as _parser
from .entry import ir_module


__all__ = [
    "ir_module",
    "module_attrs",
    "module_global_infos",
    "dummy_global_info",
    "Range",
]
