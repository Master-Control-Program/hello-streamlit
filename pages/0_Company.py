# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import streamlit as st

# Set page config to use wide mode and dark theme
st.set_page_config(layout="wide")

# Set the page title
st.set_page_config(page_title="System Ref")

# Page title
st.title('System Ref')

# Text input boxes
system_code = st.text_input('System Code')
cast_system_id = st.text_input('Cast System ID')
system_name = st.text_input('System Name')
system_alias = st.text_input('System Alias')

# Dropdown box for "Order By:"
order_by = st.selectbox(
    'Order By:',
    ('System Code', 'Cast System ID', 'System Name', 'System Alias')
)

# Function to clear the inputs
def clear_inputs():
    st.session_state['system_code'] = ''
    st.session_state['cast_system_id'] = ''
    st.session_state['system_name'] = ''
    st.session_state['system_alias'] = ''

# Search and Clear buttons
if st.button('Search'):
    st.write('Search clicked!')
    # Implement search functionality here

if st.button('Clear', on_click=clear_inputs):
    st.write('Inputs cleared!')

