# -*- coding: utf-8 -*-
#
# Entry point for the add-on into Anki
# Please do not edit this if you do not know what you are doing.
#
# Copyright: (c) 2017 Glutanimate <https://glutanimate.com/>
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

# from . import reviewer_progress_bar
from . import shige_progress_bar


from aqt import  mw, QAction, gui_hooks
from .shige_config.progressbar_config import SetProgressbarConfig, set_gui_hook_rate_this
from aqt.utils import qconnect
# ----- add-onのconfigをｸﾘｯｸしたら設定ｳｨﾝﾄﾞｳを開く -----
def add_config_button():
    mw.addonManager.setConfigAction(__name__, SetProgressbarConfig)
    # ----- ﾒﾆｭｰﾊﾞｰに追加 -----
    addon_Action = QAction("Progress bar (Fork by Shige) Settings", mw)
    qconnect(addon_Action.triggered, SetProgressbarConfig)
    mw.form.menuTools.addAction(addon_Action)

set_gui_hook_rate_this()
gui_hooks.main_window_did_init.append(add_config_button)
