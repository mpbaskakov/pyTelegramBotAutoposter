# -*- coding: utf-8 -*
import os

token = os.environ['TOKEN_AUTOPOSTER']
chat_id = os.environ['CHAT_ID_AUTOPOSTER'].split(', ')
database_url = os.environ['DATABASE_URL']
port = int(os.environ.get('PORT'))
post_int = int(os.environ.get('POST_INTERVAL'))
webhook_url = os.environ.get('WEBHOOK_URL')
bclink = os.environ.get('BCLINK')
bctest = os.environ.get('BCTEST')
