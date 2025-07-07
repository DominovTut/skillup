import enum


DAILY_BASE_QUEST_REWARD = 10
WEEKLY_BASE_QUEST_REWARD = 70
MONTHLY_BASE_QUEST_REWARD = 300

EASY_QUEST_MULTIPLIER = 1
MEDIUM_QUEST_MULTIPLIER = 3
HARD_QUEST_MULTIPLIER = 6


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

