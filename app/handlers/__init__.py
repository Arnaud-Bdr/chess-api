from chess import uci
from tornado.options import options

engine = uci.popen_engine(options.path_to_engine)
engine.uci()
localOptions = { "Skill Level" : 5 }
engine.setoption(localOptions)


from .base import BaseHandler
from .index import IndexHandler
from .game import GameHandler
