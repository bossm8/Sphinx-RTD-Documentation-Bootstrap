from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from argparse import ArgumentParser
from pathlib import Path
from os.path import join, exists
from subprocess import run
from httpwatcher import HttpWatcherServer
from tornado.ioloop import IOLoop

_patterns = ['*.md', '*.rst', '*.txt']
_path = Path(__file__).parent.resolve()

_server = HttpWatcherServer(
    static_root='build/html',
    port=3000,
    host='127.0.0.1',
    watcher_interval=2.0,
    recursive=True,
    open_browser=True
)


class BuildHandler(PatternMatchingEventHandler):
    def __init__(self):
        PatternMatchingEventHandler.__init__(self,
                                             patterns=_patterns)

    def on_modified(self, event):
        build()


def build():
    run(['make', 'html'], cwd=_path)
    pass


def watch():
    if not exists("build/html"):
        build()

    _server.listen()

    observer = Observer()
    observer.schedule(event_handler=BuildHandler(),
                      path=join(_path, "source"),
                      recursive=True)
    observer.start()

    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        observer.stop()
        _server.shutdown()
    finally:
        observer.join()


def setup():
    pass


def main():
    parser = ArgumentParser()
    sub_parsers = parser.add_subparsers()

    sub_parsers.add_parser('watch', help="Watch and build on file changes") \
        .set_defaults(func=watch)

    sub_parsers.add_parser('setup', help="Setup the project") \
        .set_defaults(func=setup)

    option = parser.parse_args()

    if hasattr(option, 'func'):
        option.func()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
