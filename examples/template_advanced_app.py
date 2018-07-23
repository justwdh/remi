"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import remi.gui as gui
from remi import start, App
import os

class MyApp(App):
    def __init__(self, *args):
        #custom additional html head tags
        my_html_head = """
            """

        #custom css
        my_css_head = """
            <link rel="stylesheet" href="" type="text/css">
            """

        #custom js
        my_js_head = """
            <script></script>
            """

        res_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res')
        #static_file_path can be an array of strings allowing to define
        #  multiple resource path in where the resources will be placed
        super(MyApp, self).__init__(*args, static_file_path=res_path, html_head=my_html_head, css_head=my_css_head, js_head=my_js_head)

    def idle(self):
        """ Idle loop, you can place here custom code,
             avoid to use infinite iterations, it would stop gui update.
            This is a Thread safe method where you can update the 
             gui with information from external Threads.
        """
        pass

    def main(self):
        #creating a container VBox type, vertical (you can use also HBox or Widget)
        main_container = gui.VBox(width=300, height=200, style={'margin':'0px auto'})

        # returning the root widget
        return main_container
                
    def on_close(self):
        """ Overloading App.on_close event allows to perform some 
             activities before app termination.
        """
        super(MyApp, self).on_close()


if __name__ == "__main__":
    # starts the webserver
    start(MyApp, address='0.0.0.0', port=0, host_name=None, start_browser=True, username=None, password=None)
