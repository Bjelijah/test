from MyStructUtil import Structure


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
