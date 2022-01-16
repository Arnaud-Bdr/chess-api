from chess import uci
from tornado.options import options

engine = uci.popen_engine(options.path_to_engine)
engine.uci()
localOptions = { "UCI_LimitStrength" : True, "UCI_Elo" : 1350, "Skill Level" : 1}
engine.setoption(localOptions)


from .base import BaseHandler
from .index import IndexHandler
from .game import GameHandler
