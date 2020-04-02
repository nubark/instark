from abc import ABC, abstractmethod
from typing import List, Union, Dict, Any
from ..models import Device, Channel, Message, Subscription
from ..repositories import (
    DeviceRepository, ChannelRepository, MessageRepository,
    SubscriptionRepository)
from ..utilities import RecordList, QueryDomain


class InstarkInformer(ABC):
    @abstractmethod
    async def search(self,
                     model: str,
                     domain: QueryDomain = None,
                     limit: int = 0,
                     offset: int = 0) -> RecordList:
        """Returns a list of <<model>> dictionaries matching the domain"""

    @abstractmethod
    async def count(self,
                    model: str,
                    domain: QueryDomain = None) -> int:
        """Returns a the <<model>> records count"""


class StandardInstarkInformer(InstarkInformer):
    def __init__(self, device_repository: DeviceRepository,
                 channel_repository: ChannelRepository,
                 message_repository: MessageRepository,
                 subscription_repository: SubscriptionRepository
                 ) -> None:
        self.device_repository = device_repository
        self.channel_repository = channel_repository
        self.message_repository = message_repository
        self.subscription_repository = subscription_repository

    async def search(self,
                     model: str,
                     domain: QueryDomain = None,
                     limit: int = 1000,
                     offset: int = 0) -> RecordList:
        repository = getattr(self, f'{model}_repository')
        return [vars(entity) for entity in
                await repository.search(
                domain or [], limit=limit, offset=offset)]

    async def count(self,
                    model: str,
                    domain: QueryDomain = None) -> int:
        repository = getattr(self, f'{model}_repository')
        return await repository.count(domain or [])
