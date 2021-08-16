- I used Django to build my backend. Looking back might have been easier to use Flask but I had more experience using Django. 

- After making the api call I save the objects/posts into my database. I would have liked to add logic for it to check the database first for unique tags instead of making the api call if it found any and then just return/render those.

- Mine also only allows one tag at a time to be queried.

- In the command line:

1. git clone https://github.com/samuelclark907/backend-assessment.git

2. poetry install ----> add dependencies

3. navigate into 'blog' directory

4. python3 manage.py runserver