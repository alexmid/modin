# Licensed to Modin Development Team under one or more contributor license agreements.
# See the NOTICE file distributed with this work for additional information regarding
# copyright ownership.  The Modin Development Team licenses this file to you under the
# Apache License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

import pytest
import pandas
import matplotlib
import modin.pandas as pd

from modin.pandas.test.utils import (
    df_equals,
    axis_values,
    axis_keys,
)

pd.DEFAULT_NPARTITIONS = 4

# Force matplotlib to not use any Xwindows backend.
matplotlib.use("Agg")


@pytest.mark.parametrize("axis", axis_values, ids=axis_keys)
def test_cummax_int_and_float(axis):
    data = {"col1": list(range(1000)), "col2": [i * 0.1 for i in range(1000)]}
    modin_df = pd.DataFrame(data)
    pandas_df = pandas.DataFrame(data)
    df_equals(modin_df.cummax(axis=axis), pandas_df.cummax(axis=axis))
