# -*- coding: utf-8 -*-
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7207, debug=True, threaded=True)


# gunicorn -k egg:meinheld#gunicorn_worker -w 2 -b 0.0.0.0:7207 main:app