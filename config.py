from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from dotenv.main import load_dotenv
from core.database import Database
import os


load_dotenv()

bot = Bot(os.environ['BOT_TOKEN'], parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database(host='localhost',
              user=os.environ['DATABASE_USER'],
              password=os.environ['DATABASE_PASSWORD'],
              port=5432,
              dbname=os.environ['DATABASE_NAME'])


