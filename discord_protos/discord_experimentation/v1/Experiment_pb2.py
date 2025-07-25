# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: discord_experimentation/v1/Experiment.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'discord_experimentation/v1/Experiment.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+discord_experimentation/v1/Experiment.proto\x12)discord_protos.discord_experimentation.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x80>\n\nExperiment\x12\n\n\x02id\x18\x01 \x01(\x06\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x33\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x12\x12\n\ncreator_id\x18\x04 \x01(\x06\x12\x0f\n\x07version\x18\x05 \x01(\x05\x12\x32\n\tedited_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x12\x11\n\teditor_id\x18\x07 \x01(\x06\x12\r\n\x05title\x18\x08 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\x35\n\nhypothesis\x18\n \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x02\x88\x01\x01\x12\x39\n\x0etech_spec_link\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x03\x88\x01\x01\x12\x10\n\x08revision\x18\x0c \x01(\x05\x12\x10\n\x08hash_key\x18\r \x01(\t\x12Q\n\tunit_type\x18\x0e \x01(\x0e\x32>.discord_protos.discord_experimentation.v1.Experiment.UnitType\x12O\n\x08variants\x18\x0f \x03(\x0b\x32=.discord_protos.discord_experimentation.v1.Experiment.Variant\x12I\n\x05rules\x18\x10 \x03(\x0b\x32:.discord_protos.discord_experimentation.v1.Experiment.Rule\x12L\n\x06status\x18\x12 \x01(\x0e\x32<.discord_protos.discord_experimentation.v1.Experiment.Status\x12O\n\x08surfaces\x18\x13 \x03(\x0e\x32=.discord_protos.discord_experimentation.v1.Experiment.Surface\x12\x18\n\x10owning_team_name\x18\x14 \x01(\t\x12&\n\x1e\x63\x61\x63hed_notification_channel_id\x18\x15 \x01(\x06\x12\x61\n\x11\x65xposure_tracking\x18\x16 \x01(\x0e\x32\x46.discord_protos.discord_experimentation.v1.Experiment.ExposureTracking\x12]\n\x0f\x61ssignment_mode\x18\x19 \x01(\x0e\x32\x44.discord_protos.discord_experimentation.v1.Experiment.AssignmentMode\x12\x1f\n\x17\x65nable_edit_raw_json_ui\x18\x17 \x01(\x08\x12\x1a\n\x12winning_variant_id\x18\x18 \x01(\x05\x1az\n\x11VariantAllocation\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0c\n\x04stop\x18\x02 \x01(\x05\x12H\n\x04type\x18\x03 \x01(\x0e\x32:.discord_protos.discord_experimentation.v1.Experiment.Type\x1a\xcc\x01\n\x07Variant\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05label\x18\x02 \x01(\t\x12\\\n\x0b\x61llocations\x18\x04 \x03(\x0b\x32G.discord_protos.discord_experimentation.v1.Experiment.VariantAllocation\x12H\n\x04type\x18\x05 \x01(\x0e\x32:.discord_protos.discord_experimentation.v1.Experiment.Type\x1a\xa1\x01\n\x18PlatformVersionSpecifier\x12\r\n\x05major\x18\x01 \x01(\r\x12\x30\n\x05minor\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueH\x00\x88\x01\x01\x12\x30\n\x05\x62uild\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueH\x01\x88\x01\x01\x42\x08\n\x06_minorB\x08\n\x06_build\x1a\xa0\x01\n\x19PlatformVersionRangeBound\x12\x64\n\x07version\x18\x01 \x01(\x0b\x32N.discord_protos.discord_experimentation.v1.Experiment.PlatformVersionSpecifierH\x00\x88\x01\x01\x12\x11\n\tinclusive\x18\x02 \x01(\x08\x42\n\n\x08_version\x1a\x8c\x02\n\x14PlatformVersionRange\x12i\n\x0blower_bound\x18\x01 \x01(\x0b\x32O.discord_protos.discord_experimentation.v1.Experiment.PlatformVersionRangeBoundH\x00\x88\x01\x01\x12i\n\x0bupper_bound\x18\x02 \x01(\x0b\x32O.discord_protos.discord_experimentation.v1.Experiment.PlatformVersionRangeBoundH\x01\x88\x01\x01\x42\x0e\n\x0c_lower_boundB\x0e\n\x0c_upper_bound\x1a\x8c\x01\n\x0fPlatformVersion\x12Z\n\x06ranges\x18\x01 \x03(\x0b\x32J.discord_protos.discord_experimentation.v1.Experiment.PlatformVersionRange\x12\x1d\n\x15work_around_pyoto_bug\x18\x02 \x01(\x08\x1a\xe2\x03\n\x0e\x43lientPlatform\x12_\n\x0bios_version\x18\x01 \x01(\x0b\x32\x45.discord_protos.discord_experimentation.v1.Experiment.PlatformVersionH\x00\x88\x01\x01\x12\x63\n\x0f\x61ndroid_version\x18\x02 \x01(\x0b\x32\x45.discord_protos.discord_experimentation.v1.Experiment.PlatformVersionH\x01\x88\x01\x01\x12_\n\x0bweb_version\x18\x03 \x01(\x0b\x32\x45.discord_protos.discord_experimentation.v1.Experiment.PlatformVersionH\x02\x88\x01\x01\x12\x62\n\x0enative_version\x18\x04 \x01(\x0b\x32\x45.discord_protos.discord_experimentation.v1.Experiment.PlatformVersionH\x03\x88\x01\x01\x42\x0e\n\x0c_ios_versionB\x12\n\x10_android_versionB\x0e\n\x0c_web_versionB\x11\n\x0f_native_version\x1a&\n\x13SDKVersionSpecifier\x12\x0f\n\x07version\x18\x01 \x01(\x05\x1a\x96\x01\n\x14SDKVersionRangeBound\x12_\n\x07version\x18\x01 \x01(\x0b\x32I.discord_protos.discord_experimentation.v1.Experiment.SDKVersionSpecifierH\x00\x88\x01\x01\x12\x11\n\tinclusive\x18\x02 \x01(\x08\x42\n\n\x08_version\x1a\xfd\x01\n\x0fSDKVersionRange\x12\x64\n\x0blower_bound\x18\x01 \x01(\x0b\x32J.discord_protos.discord_experimentation.v1.Experiment.SDKVersionRangeBoundH\x00\x88\x01\x01\x12\x64\n\x0bupper_bound\x18\x02 \x01(\x0b\x32J.discord_protos.discord_experimentation.v1.Experiment.SDKVersionRangeBoundH\x01\x88\x01\x01\x42\x0e\n\x0c_lower_boundB\x0e\n\x0c_upper_bound\x1a\x82\x01\n\nSDKVersion\x12U\n\x06ranges\x18\x01 \x03(\x0b\x32\x45.discord_protos.discord_experimentation.v1.Experiment.SDKVersionRange\x12\x1d\n\x15work_around_pyoto_bug\x18\x02 \x01(\x08\x1a\xb5\x06\n\x15\x43lientOperatingSystem\x12Z\n\x0bios_version\x18\x01 \x01(\x0b\x32@.discord_protos.discord_experimentation.v1.Experiment.SDKVersionH\x00\x88\x01\x01\x12^\n\x0f\x61ndroid_version\x18\x02 \x01(\x0b\x32@.discord_protos.discord_experimentation.v1.Experiment.SDKVersionH\x01\x88\x01\x01\x12\\\n\rmacos_version\x18\x03 \x01(\x0b\x32@.discord_protos.discord_experimentation.v1.Experiment.SDKVersionH\x02\x88\x01\x01\x12^\n\x0fwindows_version\x18\x04 \x01(\x0b\x32@.discord_protos.discord_experimentation.v1.Experiment.SDKVersionH\x03\x88\x01\x01\x12\x62\n\x13playstation_version\x18\x05 \x01(\x0b\x32@.discord_protos.discord_experimentation.v1.Experiment.SDKVersionH\x04\x88\x01\x01\x12[\n\x0cxbox_version\x18\x06 \x01(\x0b\x32@.discord_protos.discord_experimentation.v1.Experiment.SDKVersionH\x05\x88\x01\x01\x12\\\n\rlinux_version\x18\x07 \x01(\x0b\x32@.discord_protos.discord_experimentation.v1.Experiment.SDKVersionH\x06\x88\x01\x01\x42\x0e\n\x0c_ios_versionB\x12\n\x10_android_versionB\x10\n\x0e_macos_versionB\x12\n\x10_windows_versionB\x16\n\x14_playstation_versionB\x0f\n\r_xbox_versionB\x10\n\x0e_linux_version\x1a>\n\nStaffUsers\x12\x15\n\rwork_accounts\x18\x01 \x01(\x08\x12\x19\n\x11personal_accounts\x18\x02 \x01(\x08\x1a \n\x0bUserInGuild\x12\x11\n\tguild_ids\x18\x01 \x03(\x06\x1a\x1b\n\x07UserIds\x12\x10\n\x08user_ids\x18\x01 \x03(\x06\x1a#\n\x0c\x43lientLocale\x12\x13\n\x07locales\x18\x01 \x03(\tB\x02\x10\x00\x1a\x39\n\tISORegion\x12\x13\n\x0biso_country\x18\x01 \x01(\t\x12\x17\n\x0fiso_subdivision\x18\x02 \x01(\t\x1a;\n\x05Place\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\x13\n\x0bsubdivision\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\x1a\xcc\x01\n\x08Location\x12U\n\niso_region\x18\x01 \x01(\x0b\x32?.discord_protos.discord_experimentation.v1.Experiment.ISORegionH\x00\x12\x0f\n\x05is_eu\x18\x02 \x01(\x08H\x00\x12L\n\x05place\x18\x03 \x01(\x0b\x32;.discord_protos.discord_experimentation.v1.Experiment.PlaceH\x00\x42\n\n\x08location\x1a\x63\n\x0e\x43lientLocation\x12Q\n\tlocations\x18\x01 \x03(\x0b\x32>.discord_protos.discord_experimentation.v1.Experiment.Location\x1a\x1e\n\x08\x43lientIP\x12\x12\n\x06\x62locks\x18\x01 \x03(\tB\x02\x10\x00\x1a!\n\nUserLocale\x12\x13\n\x07locales\x18\x01 \x03(\tB\x02\x10\x00\x1a\x1b\n\tUserIsBot\x12\x0e\n\x06is_bot\x18\x01 \x01(\x08\x1a\xa6\x01\n\x0cUserAgeRange\x12\x38\n\rmin_age_years\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueH\x00\x88\x01\x01\x12\x38\n\rmax_age_years\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueH\x01\x88\x01\x01\x42\x10\n\x0e_min_age_yearsB\x10\n\x0e_max_age_years\x1a\x1d\n\x0c\x46ixed64Value\x12\r\n\x05value\x18\x01 \x01(\x06\x1a\xd5\x01\n\x0bUserIDRange\x12W\n\x06min_id\x18\x01 \x01(\x0b\x32\x42.discord_protos.discord_experimentation.v1.Experiment.Fixed64ValueH\x00\x88\x01\x01\x12W\n\x06max_id\x18\x02 \x01(\x0b\x32\x42.discord_protos.discord_experimentation.v1.Experiment.Fixed64ValueH\x01\x88\x01\x01\x42\t\n\x07_min_idB\t\n\x07_max_id\x1a\x1b\n\x0bUserHasFlag\x12\x0c\n\x04mask\x18\x01 \x01(\x06\x1a\x37\n\x13UnitIdInRangeByHash\x12\x10\n\x08hash_key\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\r\x1a\x34\n\x14\x43lientReleaseChannel\x12\x1c\n\x10release_channels\x18\x01 \x03(\tB\x02\x10\x00\x1a\x17\n\x06\x41lways\x12\r\n\x05value\x18\x01 \x01(\x08\x1a)\n\x12\x43lientSystemLocale\x12\x13\n\x07locales\x18\x01 \x03(\tB\x02\x10\x00\x1a\xbf\x0c\n\x06\x46ilter\x12^\n\x0e\x63lient_version\x18\x02 \x01(\x0b\x32\x44.discord_protos.discord_experimentation.v1.Experiment.ClientPlatformH\x00\x12`\n\tclient_os\x18\x03 \x01(\x0b\x32K.discord_protos.discord_experimentation.v1.Experiment.ClientOperatingSystemH\x00\x12Q\n\x05staff\x18\x04 \x01(\x0b\x32@.discord_protos.discord_experimentation.v1.Experiment.StaffUsersH\x00\x12Z\n\ruser_in_guild\x18\x05 \x01(\x0b\x32\x41.discord_protos.discord_experimentation.v1.Experiment.UserInGuildH\x00\x12Q\n\x08user_ids\x18\x06 \x01(\x0b\x32=.discord_protos.discord_experimentation.v1.Experiment.UserIdsH\x00\x12[\n\rclient_locale\x18\x07 \x01(\x0b\x32\x42.discord_protos.discord_experimentation.v1.Experiment.ClientLocaleH\x00\x12_\n\x0f\x63lient_location\x18\x08 \x01(\x0b\x32\x44.discord_protos.discord_experimentation.v1.Experiment.ClientLocationH\x00\x12S\n\tclient_ip\x18\t \x01(\x0b\x32>.discord_protos.discord_experimentation.v1.Experiment.ClientIPH\x00\x12W\n\x0buser_locale\x18\n \x01(\x0b\x32@.discord_protos.discord_experimentation.v1.Experiment.UserLocaleH\x00\x12N\n\x03\x62ot\x18\x0b \x01(\x0b\x32?.discord_protos.discord_experimentation.v1.Experiment.UserIsBotH\x00\x12\\\n\x0euser_age_range\x18\x0c \x01(\x0b\x32\x42.discord_protos.discord_experimentation.v1.Experiment.UserAgeRangeH\x00\x12Z\n\ruser_id_range\x18\r \x01(\x0b\x32\x41.discord_protos.discord_experimentation.v1.Experiment.UserIDRangeH\x00\x12Z\n\ruser_has_flag\x18\x0e \x01(\x0b\x32\x41.discord_protos.discord_experimentation.v1.Experiment.UserHasFlagH\x00\x12m\n\x18unit_id_in_range_by_hash\x18\x0f \x01(\x0b\x32I.discord_protos.discord_experimentation.v1.Experiment.UnitIdInRangeByHashH\x00\x12l\n\x16\x63lient_release_channel\x18\x10 \x01(\x0b\x32J.discord_protos.discord_experimentation.v1.Experiment.ClientReleaseChannelH\x00\x12N\n\x06\x61lways\x18\x11 \x01(\x0b\x32<.discord_protos.discord_experimentation.v1.Experiment.AlwaysH\x00\x12h\n\x14\x63lient_system_locale\x18\x12 \x01(\x0b\x32H.discord_protos.discord_experimentation.v1.Experiment.ClientSystemLocaleH\x00\x42\x08\n\x06\x66ilter\x1a\x1e\n\x08Override\x12\x12\n\nvariant_id\x18\x01 \x01(\x05\x1a\x9b\x02\n\x04Rule\x12H\n\x04type\x18\x01 \x01(\x0e\x32:.discord_protos.discord_experimentation.v1.Experiment.Type\x12M\n\x07\x66ilters\x18\x02 \x03(\x0b\x32<.discord_protos.discord_experimentation.v1.Experiment.Filter\x12U\n\x08override\x18\x03 \x01(\x0b\x32>.discord_protos.discord_experimentation.v1.Experiment.OverrideH\x00\x88\x01\x01\x12\x16\n\x0eis_sunset_rule\x18\x04 \x01(\x08\x42\x0b\n\t_override\"9\n\x08UnitType\x12\x19\n\x15UNIT_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eUNIT_TYPE_USER\x10\x01\"O\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bTYPE_ACTIVE\x10\x01\x12\x0f\n\x0bTYPE_UNUSED\x10\x02\x12\x0f\n\x0bTYPE_BURNED\x10\x03\"\xa4\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x0cSTATUS_DRAFT\x10\x01\x12\x12\n\x0eSTATUS_TESTING\x10\x02\x12\x18\n\x14STATUS_TESTING_ENDED\x10\x03\x12\x16\n\x12STATUS_ROLLING_OUT\x10\x04\x12\x15\n\x11STATUS_ROLLED_OUT\x10\x05\x12\x13\n\x0fSTATUS_ARCHIVED\x10\x06\"D\n\x07Surface\x12\x17\n\x13SURFACE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bSURFACE_API\x10\x01\x12\x0f\n\x0bSURFACE_APP\x10\x02\"Q\n\x10\x45xposureTracking\x12\x1d\n\x19\x45XPOSURE_TRACKING_ENABLED\x10\x00\x12\x1e\n\x1a\x45XPOSURE_TRACKING_DISABLED\x10\x01\"p\n\x0e\x41ssignmentMode\x12\x18\n\x14\x41SSIGNMENT_MODE_FULL\x10\x00\x12!\n\x1d\x41SSIGNMENT_MODE_FORCE_DEFAULT\x10\x01\x12!\n\x1d\x41SSIGNMENT_MODE_OVERRIDE_ONLY\x10\x02\x42\r\n\x0b_created_atB\x0c\n\n_edited_atB\r\n\x0b_hypothesisB\x11\n\x0f_tech_spec_linkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'discord_experimentation.v1.Experiment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EXPERIMENT_CLIENTLOCALE'].fields_by_name['locales']._loaded_options = None
  _globals['_EXPERIMENT_CLIENTLOCALE'].fields_by_name['locales']._serialized_options = b'\020\000'
  _globals['_EXPERIMENT_CLIENTIP'].fields_by_name['blocks']._loaded_options = None
  _globals['_EXPERIMENT_CLIENTIP'].fields_by_name['blocks']._serialized_options = b'\020\000'
  _globals['_EXPERIMENT_USERLOCALE'].fields_by_name['locales']._loaded_options = None
  _globals['_EXPERIMENT_USERLOCALE'].fields_by_name['locales']._serialized_options = b'\020\000'
  _globals['_EXPERIMENT_CLIENTRELEASECHANNEL'].fields_by_name['release_channels']._loaded_options = None
  _globals['_EXPERIMENT_CLIENTRELEASECHANNEL'].fields_by_name['release_channels']._serialized_options = b'\020\000'
  _globals['_EXPERIMENT_CLIENTSYSTEMLOCALE'].fields_by_name['locales']._loaded_options = None
  _globals['_EXPERIMENT_CLIENTSYSTEMLOCALE'].fields_by_name['locales']._serialized_options = b'\020\000'
  _globals['_EXPERIMENT']._serialized_start=156
  _globals['_EXPERIMENT']._serialized_end=8092
  _globals['_EXPERIMENT_VARIANTALLOCATION']._serialized_start=1262
  _globals['_EXPERIMENT_VARIANTALLOCATION']._serialized_end=1384
  _globals['_EXPERIMENT_VARIANT']._serialized_start=1387
  _globals['_EXPERIMENT_VARIANT']._serialized_end=1591
  _globals['_EXPERIMENT_PLATFORMVERSIONSPECIFIER']._serialized_start=1594
  _globals['_EXPERIMENT_PLATFORMVERSIONSPECIFIER']._serialized_end=1755
  _globals['_EXPERIMENT_PLATFORMVERSIONRANGEBOUND']._serialized_start=1758
  _globals['_EXPERIMENT_PLATFORMVERSIONRANGEBOUND']._serialized_end=1918
  _globals['_EXPERIMENT_PLATFORMVERSIONRANGE']._serialized_start=1921
  _globals['_EXPERIMENT_PLATFORMVERSIONRANGE']._serialized_end=2189
  _globals['_EXPERIMENT_PLATFORMVERSION']._serialized_start=2192
  _globals['_EXPERIMENT_PLATFORMVERSION']._serialized_end=2332
  _globals['_EXPERIMENT_CLIENTPLATFORM']._serialized_start=2335
  _globals['_EXPERIMENT_CLIENTPLATFORM']._serialized_end=2817
  _globals['_EXPERIMENT_SDKVERSIONSPECIFIER']._serialized_start=2819
  _globals['_EXPERIMENT_SDKVERSIONSPECIFIER']._serialized_end=2857
  _globals['_EXPERIMENT_SDKVERSIONRANGEBOUND']._serialized_start=2860
  _globals['_EXPERIMENT_SDKVERSIONRANGEBOUND']._serialized_end=3010
  _globals['_EXPERIMENT_SDKVERSIONRANGE']._serialized_start=3013
  _globals['_EXPERIMENT_SDKVERSIONRANGE']._serialized_end=3266
  _globals['_EXPERIMENT_SDKVERSION']._serialized_start=3269
  _globals['_EXPERIMENT_SDKVERSION']._serialized_end=3399
  _globals['_EXPERIMENT_CLIENTOPERATINGSYSTEM']._serialized_start=3402
  _globals['_EXPERIMENT_CLIENTOPERATINGSYSTEM']._serialized_end=4223
  _globals['_EXPERIMENT_STAFFUSERS']._serialized_start=4225
  _globals['_EXPERIMENT_STAFFUSERS']._serialized_end=4287
  _globals['_EXPERIMENT_USERINGUILD']._serialized_start=4289
  _globals['_EXPERIMENT_USERINGUILD']._serialized_end=4321
  _globals['_EXPERIMENT_USERIDS']._serialized_start=4323
  _globals['_EXPERIMENT_USERIDS']._serialized_end=4350
  _globals['_EXPERIMENT_CLIENTLOCALE']._serialized_start=4352
  _globals['_EXPERIMENT_CLIENTLOCALE']._serialized_end=4387
  _globals['_EXPERIMENT_ISOREGION']._serialized_start=4389
  _globals['_EXPERIMENT_ISOREGION']._serialized_end=4446
  _globals['_EXPERIMENT_PLACE']._serialized_start=4448
  _globals['_EXPERIMENT_PLACE']._serialized_end=4507
  _globals['_EXPERIMENT_LOCATION']._serialized_start=4510
  _globals['_EXPERIMENT_LOCATION']._serialized_end=4714
  _globals['_EXPERIMENT_CLIENTLOCATION']._serialized_start=4716
  _globals['_EXPERIMENT_CLIENTLOCATION']._serialized_end=4815
  _globals['_EXPERIMENT_CLIENTIP']._serialized_start=4817
  _globals['_EXPERIMENT_CLIENTIP']._serialized_end=4847
  _globals['_EXPERIMENT_USERLOCALE']._serialized_start=4849
  _globals['_EXPERIMENT_USERLOCALE']._serialized_end=4882
  _globals['_EXPERIMENT_USERISBOT']._serialized_start=4884
  _globals['_EXPERIMENT_USERISBOT']._serialized_end=4911
  _globals['_EXPERIMENT_USERAGERANGE']._serialized_start=4914
  _globals['_EXPERIMENT_USERAGERANGE']._serialized_end=5080
  _globals['_EXPERIMENT_FIXED64VALUE']._serialized_start=5082
  _globals['_EXPERIMENT_FIXED64VALUE']._serialized_end=5111
  _globals['_EXPERIMENT_USERIDRANGE']._serialized_start=5114
  _globals['_EXPERIMENT_USERIDRANGE']._serialized_end=5327
  _globals['_EXPERIMENT_USERHASFLAG']._serialized_start=5329
  _globals['_EXPERIMENT_USERHASFLAG']._serialized_end=5356
  _globals['_EXPERIMENT_UNITIDINRANGEBYHASH']._serialized_start=5358
  _globals['_EXPERIMENT_UNITIDINRANGEBYHASH']._serialized_end=5413
  _globals['_EXPERIMENT_CLIENTRELEASECHANNEL']._serialized_start=5415
  _globals['_EXPERIMENT_CLIENTRELEASECHANNEL']._serialized_end=5467
  _globals['_EXPERIMENT_ALWAYS']._serialized_start=5469
  _globals['_EXPERIMENT_ALWAYS']._serialized_end=5492
  _globals['_EXPERIMENT_CLIENTSYSTEMLOCALE']._serialized_start=5494
  _globals['_EXPERIMENT_CLIENTSYSTEMLOCALE']._serialized_end=5535
  _globals['_EXPERIMENT_FILTER']._serialized_start=5538
  _globals['_EXPERIMENT_FILTER']._serialized_end=7137
  _globals['_EXPERIMENT_OVERRIDE']._serialized_start=7139
  _globals['_EXPERIMENT_OVERRIDE']._serialized_end=7169
  _globals['_EXPERIMENT_RULE']._serialized_start=7172
  _globals['_EXPERIMENT_RULE']._serialized_end=7455
  _globals['_EXPERIMENT_UNITTYPE']._serialized_start=7457
  _globals['_EXPERIMENT_UNITTYPE']._serialized_end=7514
  _globals['_EXPERIMENT_TYPE']._serialized_start=7516
  _globals['_EXPERIMENT_TYPE']._serialized_end=7595
  _globals['_EXPERIMENT_STATUS']._serialized_start=7598
  _globals['_EXPERIMENT_STATUS']._serialized_end=7762
  _globals['_EXPERIMENT_SURFACE']._serialized_start=7764
  _globals['_EXPERIMENT_SURFACE']._serialized_end=7832
  _globals['_EXPERIMENT_EXPOSURETRACKING']._serialized_start=7834
  _globals['_EXPERIMENT_EXPOSURETRACKING']._serialized_end=7915
  _globals['_EXPERIMENT_ASSIGNMENTMODE']._serialized_start=7917
  _globals['_EXPERIMENT_ASSIGNMENTMODE']._serialized_end=8029
# @@protoc_insertion_point(module_scope)
