#pip install Eel
import eel
from os import getcwd

eel.init('.')
eel.start(getcwd() + "\\realtime_editor.html", mode='chrome',
          cmdline_args=['--start-fullscreen'], port=7499)
