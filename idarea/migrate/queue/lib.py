# -*- coding: utf-8 -*-

import os
import time
import os.path
import shutil
from idarea.migrate.static import migrateObj
from idarea.common.utils import PART_SEQ,MD5_HEAD,SLEEP_INTERVAL,MD5_TEMP
from idarea.ring.variable import CURRENT_RING_SEQ
from idarea.common.utils import OBJECT_SUFFIX,MIGRATE_SUFFIX,QUEUE_TIMEOUT_INTERVAL
from idarea.ring.variable import LOAD_HOST_LIST



            