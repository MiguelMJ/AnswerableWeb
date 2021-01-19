import os
import io
from contextlib import redirect_stdout

from flask import Flask

import Answerable

app = Flask(__name__)


@app.route("/")
def hello_world():
    user = "8757033"
    f = io.StringIO()
    with redirect_stdout(f):
        Answerable.main(["--no-ansi", "-v", "summary","-u",user])
    content = f.getvalue().replace("\n","\n\r")
    print("Returning:")
    print(content)
    return content


if __name__ == "__main__":
    app.run()
    Answerable.tools.log.close_logs()
    print("Done")
