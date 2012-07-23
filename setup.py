from distutils.core import setup
import os
import subprocess

if os.path.exists("debian/changelog"):
    output=subprocess.check_output("parsechangelog | grep Version", shell=True)
    version = output.split(":")[1].strip()

setup(name = "turtlebot-indicator",
    version = version,
    description = "TurtleBot Status Indicator",
    author = "I Heart Engineering",
    author_email = "code@iheartengineering.com",
    url = "http://www.iheartengineering.com",
    license = "BSD-3-clause",
    scripts = ["turtlebot-indicator"],
    data_files = [('/usr/share/icons/hicolor/scalable/apps', ['icons/turtlebot-idle.svg', 'icons/turtlebot-panel.svg']),
                  ('/etc/xdg/autostart', ['turtlebot-indicator.desktop'])],
    long_description = """This tool displays status information about the TurtleBot.""" 
    #classifiers = []     
) 
