language: python
python:
  - "3.6"
  - "3.7"
  - "3.8"
script:
  - python greetings.py
  - python -m unittest test_greetings.py
