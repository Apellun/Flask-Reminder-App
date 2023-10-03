from project.config import Config
from project.server import create_app

app = create_app(Config)