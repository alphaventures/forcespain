# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import pyromod.listen
import sys

from pyrogram import Client, enums

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_CHANNEL,
    FORCE_SUB_GROUP,
    FORCE_SUB_CHANNELS,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
            self.LOGGER(__name__).info(
                f"TG_BOT_TOKEN detected!\n┌ First Name: {self.namebot}\n└ Username: @{self.username}\n——"
            )
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).info(
                "Detener los bots. Únete al grupo https://t.me/pelicula_series_espanols para obtener ayuda"
            )
            sys.exit()

        if FORCE_SUB_CHANNEL:
            try:
                info = await self.get_chat(FORCE_SUB_CHANNEL)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = info.invite_link
                self.invitelink = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_CHANNEL detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "El bot no puede recuperar el enlace de invitación de FORCE_SUB_CHANNEL!"
                )
                self.LOGGER(__name__).warning(
                    f"Asegúrese de que @{self.username} sea un administrador en el canal, Id. de chat del canal actual F-Subs: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "Detener los bots. Únase al grupo https://t.me/SharingUserbot para obtener ayuda"
                )
                sys.exit()

        if FORCE_SUB_GROUP:
            try:
                info = await self.get_chat(FORCE_SUB_GROUP)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP)
                    link = info.invite_link
                self.invitelink2 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_GROUP detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "El bot no puede recuperar el enlace de invitación de FORCE_SUB_GROUP!"
                )
                self.LOGGER(__name__).warning(
                    f"Cerciorarse @{self.username} es el administrador del grupo, ID de chat actual F-Subs Group: {FORCE_SUB_GROUP}"
                )
                self.LOGGER(__name__).info(
                    "Detener los bots. Únase al grupo https://t.me/SharingUserbot para obtener ayuda"
                )
                sys.exit()
        if FORCE_SUB_CHANNELS:
            try:
                info = await self.get_chat(FORCE_SUB_CHANNELS)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNELS)
                    link = info.invite_link
                self.invitelink1 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_CHANNEL detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "El bot no puede recuperar el enlace de invitación de FORCE_SUB_CHANNEL!"
                )
                self.LOGGER(__name__).warning(
                    f"Cerciorarse @{self.username} es el administrador del canal, ID de chat del canal actual F-Subs: {FORCE_SUB_CHANNELS}"
                )
                self.LOGGER(__name__).info(
                    "Detener los bots. Únase al grupo https://t.me/SharingUserbot para obtener ayuda"
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message", disable_notification=True)
            await test.delete()
            self.LOGGER(__name__).info(
                f"CHANNEL_ID Database detected!\n┌ Title: {db_channel.title}\n└ Chat ID: {db_channel.id}\n——"
            )
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Cerciorarse @{self.username} es el administrador de su base de datos de canales, CHANNEL_ID actual: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "Detener los bots. Únase a Groupps://t.me/SharingUserbot para obtener ayuda"
            )
            sys.exit()

        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"[🔥 ¡ACTIVADO CON ÉXITO! 🔥]\n\nBOT Creado por @{OWNER}\nSi @{OWNER} necesita ayuda, pregunte en el grupo https://t.me/SharingUserbot"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")