from dataclasses import dataclass, field
from core.configurations.ConfigurationBase import ConfigurationBase

from enum import Enum

class DungeonDifficulty(Enum):
    NORMAL = "NORMAL"
    HARD = "HARD"
    HEROIC = "HEROIC"

ENERGY_DIFFICULTY = {
    DungeonDifficulty.NORMAL: 10,
    DungeonDifficulty.HARD: 20,
    DungeonDifficulty.HEROIC: 30
}

ENERGY_COOLDOWN = 240 # in seconds

@dataclass
class AutoQuestConfiguration(ConfigurationBase):

    is_enabled: bool = True
    zone: int = 0
    dungeon: int = 0
    difficulty: DungeonDifficulty = DungeonDifficulty.HEROIC
    is_persuasion_enabled: bool = True
    auto_decline_familiar: bool = True
    familiar_names: list[str] = field(default_factory=list)

    def __init__(self, file_path: str):
        self.familiar_names = []
        super().__init__(file_path)