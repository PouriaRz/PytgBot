# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class Update(Result):
    """
    This object represents an incoming update. Only one of the optional parameters can be present in any given update.

    https://core.telegram.org/bots/api#update
    """
    def __init__(self, update_id, message = None, inline_query = None, chosen_inline_result = None, callback_query = None):
        """
        This object represents an incoming update.Only one of the optional parameters can be present in any given update.

        https://core.telegram.org/bots/api#update


        Parameters:

        :param update_id: The update‘s unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you’re using Webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order.
        :type  update_id:  int


        Optional keyword parameters:

        :keyword message: Optional. New incoming message of any kind — text, photo, sticker, etc.
        :type    message:  Message

        :keyword inline_query: Optional. New incoming inline query
        :type    inline_query:  InlineQuery

        :keyword chosen_inline_result: Optional. The result of an inline query that was chosen by a user and sent to their chat partner.
        :type    chosen_inline_result:  ChosenInlineResult

        :keyword callback_query: Optional. New incoming callback query
        :type    callback_query:  CallbackQuery
        """
        super(Update, self).__init__(id)

        assert(update_id is not None)
        assert(isinstance(update_id, int))
        self.update_id = update_id

        self.message = message

        self.inline_query = inline_query

        self.chosen_inline_result = chosen_inline_result

        self.callback_query = callback_query
    # end def __init__

    def to_array(self):
        array = super(Update, self).to_array()
        array["update_id"] = self.update_id
        if self.message is not None:
            array["message"] = self.message
        if self.inline_query is not None:
            array["inline_query"] = self.inline_query
        if self.chosen_inline_result is not None:
            array["chosen_inline_result"] = self.chosen_inline_result
        if self.callback_query is not None:
            array["callback_query"] = self.callback_query
        return array
    # end def to_array
# end class Update


class Message(Result):
    """
    This object represents a message.

    https://core.telegram.org/bots/api#message
    """
    def __init__(self, message_id, date, chat, from_peer = None, forward_from = None, forward_date = None, reply_to_message = None, text = None, entities = None, audio = None, document = None, photo = None, sticker = None, video = None, voice = None, caption = None, contact = None, location = None, venue = None, new_chat_member = None, left_chat_member = None, new_chat_title = None, new_chat_photo = None, delete_chat_photo = None, group_chat_created = None, supergroup_chat_created = None, channel_chat_created = None, migrate_to_chat_id = None, migrate_from_chat_id = None, pinned_message = None):
        """
        This object represents a message.

        https://core.telegram.org/bots/api#message


        Parameters:

        :param message_id: Unique message identifier
        :type  message_id:  int

        :param date: Date the message was sent in Unix time
        :type  date:  int

        :param chat: Conversation the message belongs to
        :type  chat:  Chat


        Optional keyword parameters:

        :keyword from_peer: Optional. Sender, can be empty for messages sent to channels
        :type    from_peer:  User

        :keyword forward_from: Optional. For forwarded messages, sender of the original message
        :type    forward_from:  User

        :keyword forward_date: Optional. For forwarded messages, date the original message was sent in Unix time
        :type    forward_date:  int

        :keyword reply_to_message: Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
        :type    reply_to_message:  Message

        :keyword text: Optional. For text messages, the actual UTF-8 text of the message, 0-4096 characters.
        :type    text:  str

        :keyword entities: Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
        :type    entities:  Array of MessageEntity

        :keyword audio: Optional. Message is an audio file, information about the file
        :type    audio:  pytgbot.api_types.responses.media.Audio

        :keyword document: Optional. Message is a general file, information about the file
        :type    document:  pytgbot.api_types.responses.media.Document

        :keyword photo: Optional. Message is a photo, available sizes of the photo
        :type    photo:  Array of PhotoSize

        :keyword sticker: Optional. Message is a sticker, information about the sticker
        :type    sticker:  pytgbot.api_types.responses.media.Sticker

        :keyword video: Optional. Message is a video, information about the video
        :type    video:  pytgbot.api_types.responses.media.Video

        :keyword voice: Optional. Message is a voice message, information about the file
        :type    voice:  Voice

        :keyword caption: Optional. Caption for the document, photo or video, 0-200 characters
        :type    caption:  str

        :keyword contact: Optional. Message is a shared contact, information about the contact
        :type    contact:  Contact

        :keyword location: Optional. Message is a shared location, information about the location
        :type    location:  Location

        :keyword venue: Optional. Message is a venue, information about the venue
        :type    venue:  Venue

        :keyword new_chat_member: Optional. A new member was added to the group, information about them (this member may be the bot itself)
        :type    new_chat_member:  User

        :keyword left_chat_member: Optional. A member was removed from the group, information about them (this member may be the bot itself)
        :type    left_chat_member:  User

        :keyword new_chat_title: Optional. A chat title was changed to this value
        :type    new_chat_title:  str

        :keyword new_chat_photo: Optional. A chat photo was change to this value
        :type    new_chat_photo:  Array of PhotoSize

        :keyword delete_chat_photo: Optional. Service message: the chat photo was deleted
        :type    delete_chat_photo:  True

        :keyword group_chat_created: Optional. Service message: the group has been created
        :type    group_chat_created:  True

        :keyword supergroup_chat_created: Optional. Service message: the supergroup has been created
        :type    supergroup_chat_created:  True

        :keyword channel_chat_created: Optional. Service message: the channel has been created
        :type    channel_chat_created:  True

        :keyword migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier, not exceeding 1e13 by absolute value
        :type    migrate_to_chat_id:  int

        :keyword migrate_from_chat_id: Optional. The supergroup has been migrated from a group with the specified identifier, not exceeding 1e13 by absolute value
        :type    migrate_from_chat_id:  int

        :keyword pinned_message: Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
        :type    pinned_message:  Message
        """
        super(Message, self).__init__(id)

        assert(message_id is not None)
        assert(isinstance(message_id, int))
        self.message_id = message_id

        self.from_peer = from_peer

        assert(date is not None)
        assert(isinstance(date, int))
        self.date = date

        self.chat = chat

        self.forward_from = forward_from

        assert(forward_date is None or isinstance(forward_date, int))
        self.forward_date = forward_date

        self.reply_to_message = reply_to_message

        assert(text is None or isinstance(text, unicode_type))  # unicode on python 2, str on python 3
        self.text = text

        assert(entities is None or isinstance(entities, (list, tuple)))  # Array of MessageEntity
        self.entities = entities

        self.audio = audio

        self.document = document

        assert(photo is None or isinstance(photo, (list, tuple)))  # Array of PhotoSize
        self.photo = photo

        self.sticker = sticker

        self.video = video

        self.voice = voice

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.contact = contact

        self.location = location

        self.venue = venue

        self.new_chat_member = new_chat_member

        self.left_chat_member = left_chat_member

        assert(new_chat_title is None or isinstance(new_chat_title, unicode_type))  # unicode on python 2, str on python 3
        self.new_chat_title = new_chat_title

        assert(new_chat_photo is None or isinstance(new_chat_photo, (list, tuple)))  # Array of PhotoSize
        self.new_chat_photo = new_chat_photo

        self.delete_chat_photo = delete_chat_photo

        self.group_chat_created = group_chat_created

        self.supergroup_chat_created = supergroup_chat_created

        self.channel_chat_created = channel_chat_created

        assert(migrate_to_chat_id is None or isinstance(migrate_to_chat_id, int))
        self.migrate_to_chat_id = migrate_to_chat_id

        assert(migrate_from_chat_id is None or isinstance(migrate_from_chat_id, int))
        self.migrate_from_chat_id = migrate_from_chat_id

        self.pinned_message = pinned_message
    # end def __init__

    def to_array(self):
        array = super(Message, self).to_array()
        array["message_id"] = self.message_id
        array["date"] = self.date
        array["chat"] = self.chat
        if self.from_peer is not None:
            array["from_peer"] = self.from_peer
        if self.forward_from is not None:
            array["forward_from"] = self.forward_from
        if self.forward_date is not None:
            array["forward_date"] = self.forward_date
        if self.reply_to_message is not None:
            array["reply_to_message"] = self.reply_to_message
        if self.text is not None:
            array["text"] = self.text
        if self.entities is not None:
            array["entities"] = self.entities
        if self.audio is not None:
            array["audio"] = self.audio
        if self.document is not None:
            array["document"] = self.document
        if self.photo is not None:
            array["photo"] = self.photo
        if self.sticker is not None:
            array["sticker"] = self.sticker
        if self.video is not None:
            array["video"] = self.video
        if self.voice is not None:
            array["voice"] = self.voice
        if self.caption is not None:
            array["caption"] = self.caption
        if self.contact is not None:
            array["contact"] = self.contact
        if self.location is not None:
            array["location"] = self.location
        if self.venue is not None:
            array["venue"] = self.venue
        if self.new_chat_member is not None:
            array["new_chat_member"] = self.new_chat_member
        if self.left_chat_member is not None:
            array["left_chat_member"] = self.left_chat_member
        if self.new_chat_title is not None:
            array["new_chat_title"] = self.new_chat_title
        if self.new_chat_photo is not None:
            array["new_chat_photo"] = self.new_chat_photo
        if self.delete_chat_photo is not None:
            array["delete_chat_photo"] = self.delete_chat_photo
        if self.group_chat_created is not None:
            array["group_chat_created"] = self.group_chat_created
        if self.supergroup_chat_created is not None:
            array["supergroup_chat_created"] = self.supergroup_chat_created
        if self.channel_chat_created is not None:
            array["channel_chat_created"] = self.channel_chat_created
        if self.migrate_to_chat_id is not None:
            array["migrate_to_chat_id"] = self.migrate_to_chat_id
        if self.migrate_from_chat_id is not None:
            array["migrate_from_chat_id"] = self.migrate_from_chat_id
        if self.pinned_message is not None:
            array["pinned_message"] = self.pinned_message
        return array
    # end def to_array
# end class Message