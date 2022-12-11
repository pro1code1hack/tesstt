from console import turn_off_pc
from internet import google_info
from notepad import save_data
from weather import get_weather

commands = {
    'turn off pc': turn_off_pc,
    'help': None,
    'send money': None,
    'google': google_info,
    'random image': None,
    'translate': None,
    'open notepad': save_data,
    'weather': get_weather,
    'currency': None
}
