import os

#
# Supported database:
#   1. mongo
#

db = 'mongo'

# Reminders

REMIND_COMMAND = '%s/penenv/bin/python %s/bin/crons/remind_cron.py' % (os.getcwd(), os.getcwd())


# Webcomics

XKCD_CRAWLER_URL = 'http://xkcd.com/archive/'
