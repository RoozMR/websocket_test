# websocket_test
First of all clone the project and then create a virtualenv inside root folder and activate it.

Then run `pip install -r requirements.txt`.

Apply migrations with `python manage.py migrate` command.

Now you will be able to run a local server using `python manage.py runserver`.

A websocket echo consumer will be available at `ws://localhost:8000/ws/echo/`, you can see a minimal html form at `localhost:8000/` which uses the echo websocket
(See [echo.html](templates/echo.html) for further information).
