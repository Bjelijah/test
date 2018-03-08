from MyStructUtil import Structure


HW_PROTOCOL_LOGIN = 0xff000001


class HwMediaInfo(Structure):
    _fields_ = [
        ('I', 'media_fourcc'),
        ('l', 'dvr_version'),
        ('l', 'vdec_code'),
        ('l', 'adec_code'),
        ('B', 'au_bits'),
        ('B', 'au_sample'),
        ('B', 'au_channel'),
        ('B', 'reserve'),
        ('5I', 'reserved')
    ]


class StreamHead(Structure):
    _fields_ = [
        ('l', 'len'),
        ('l', 'type'),
        ('Q', 'time_stamp'),
        ('l', 'tag'),
        ('l', 'sys_time')
    ]


class ProtocolHead(Structure):
    _fields_ = [
        ('I', 'proType'),
        ('I', 'proVersion'),
        ('I', 'dataLen'),
        ('I', 'proMinVersion'),
        ('I', 'err'),
        ('I', 'seq_num'),
        ('29I', 'reserved')
    ]


class TLogin(Structure):
    _fields_ = [
        ('i', 'type'),
        ('32c', 'logName'),
        ('32c', 'logPassword'),
        ('i', 'clientUserID'),
        ('32i', 'reserved')
    ]
