#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template


class YourFlask(Flask):
    def create_jinja_environment(self):
        self.config['TEMPLATES_AUTO_RELOAD'] = True
        return Flask.create_jinja_environment(self)
app = YourFlask(__name__)
# app = Flask(__name__)

app.jinja_env.line_statement_prefix = '%'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('base.html', raw_content="pastes for all :)")


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Development Server Help')
    parser.add_argument("-d", "--debug", action="store_true",
                        dest="debug_mode",
                        help="run in debug mode (for use with PyCharm)",
                        default=False)
    parser.add_argument("-p", "--port", dest="port",
                        help="port of server (default:%(default)s)",
                        type=int, default=5000)
    cmd_args = parser.parse_args()
    app_options = {"port": cmd_args.port}

    # if cmd_args.debug_mode:
    #     app.port = cmd_args.port
    #     app.debug = True
    # app.run()

    app_options["debug"] = cmd_args.debug_mode
    if cmd_args.debug_mode:
        app_options["use_debugger"] = False
        app_options["use_reloader"] = False

    app.run(**app_options)


if __name__ == '__main__':
    main()
