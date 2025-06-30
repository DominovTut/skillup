import enum


class QuestTypes(enum.Enum):
    daily = "DAILY"
    weekly = "WEEKLY"
    monthly = "MONTHLY"


class QuestStatus(enum.Enum):
    in_progress = "IN_PROGRESS"
    done = "DONE"
    canceled = "CANCELED"


class QuestDifficulty(enum.Enum):
    easy = "EASY"
    medium = "MEDIUM"
    hard = "HARD"

