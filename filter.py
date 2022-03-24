from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from constant import admin


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        member = message.from_user.id
        return member in admin