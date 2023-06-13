import os
# project_path = os.path.dirname(os.path.realpath(__file__))
# #  C:\GitHub\venv2\veego_tester\:
# results_folder = f"{project_path}/test_results"
# python_venv = f"{project_path}/venv/Scripts/python.py"
# mobile_main = f"{project_path}/mobile_main.py"
# main = f"{project_path}/main.py"
# os.system(f"python -m pytest -vv --alluredir={results_folder}{python_venv} {mobile_main}")
# os.system(f"python -m pytest -vv --alluredir={results_folder}  {python_venv} {main}")


os.system(f"python -m pytest -vv --alluredir=C:/GitHub/venv2/veego_tester/ C:/GitHub/venv2/veego_tester/mobile_main.py")