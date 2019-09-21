from typing import Dict, Any
from ..configuration import Config
from .factory import Factory
from .memory_factory import MemoryFactory
from .http_factory import HttpFactory
from .trial_factory import TrialFactory


def build_factory(config: Config) -> Factory:
    factory = config['factory']
    return {
        'MemoryFactory': lambda config: MemoryFactory(config),
        'TrialFactory': lambda config: TrialFactory(config),
        'HttpFactory': lambda config: HttpFactory(config),
    }[factory](config)
