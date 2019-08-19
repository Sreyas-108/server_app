import enum


class ModuleType(enum.Enum):
    """Module type of OSC data."""
    FEEDBACK = -3, "/feedback"
    SHARE = -2, "/share"
    EXIT = -1, "/exit"
    GESTURE = 0, "/gesture"
    FLYTO = 1, "/flyto"
    POI = 2, "/poi"
    TOUR = 3, "/tour"
    OVERLAY = 4, "/overlay"
