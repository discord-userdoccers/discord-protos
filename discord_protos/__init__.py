from __future__ import annotations

from enum import Enum as _Enum
from typing import TYPE_CHECKING

__version__ = '1.2.89'

if TYPE_CHECKING:
    from google.protobuf.message import Message as _Message

    User = MediumUser = UserData = GuildShardingConfig = PreloadedUserSettings = FrecencyUserSettings = Experiment = ApplicationUserRoleConnection = AcknowledgedApplicationDisclosures = PremiumMarketingComponentProperties = _Message
else:
    from .users.v1.User_pb2 import *
    from .users.v1.MediumUser_pb2 import *
    from .users.v1.UserData_pb2 import *
    from .users.v1.GuildShardingConfig_pb2 import *
    from .discord_users.v1.PreloadedUserSettings_pb2 import *
    from .discord_users.v1.FrecencyUserSettings_pb2 import *
    from .discord_experimentation.v1.Experiment_pb2 import *
    from .discord_kkv_store_value_models.v1.ApplicationUserRoleConnection_pb2 import *
    from .discord_kkv_store_value_models.v1.AcknowledgedApplicationDisclosures_pb2 import *
    from .premium_marketing.v1.PremiumMarketingComponentProperties_pb2 import *

__all__ = (
    '__version__',
    'UserSettingsType',
    'User',
    'MediumUser',
    'UserData',
    'GuildShardingConfig',
    'PreloadedUserSettings',
    'FrecencyUserSettings',
    'Experiment',
    'ApplicationUserRoleConnection',
    'AcknowledgedApplicationDisclosures',
    'PremiumMarketingComponentProperties',
)


class UserSettingsType(_Enum):
    preloaded_user_settings = 1
    frecency_user_settings = 2
    test_settings = 3


UserSettingsImpl = {
    UserSettingsType.preloaded_user_settings: PreloadedUserSettings,
    UserSettingsType.frecency_user_settings: FrecencyUserSettings,
    UserSettingsType.test_settings: None,
}
