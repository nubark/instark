from pytest import fixture
from instark.application.domain.repositories import (
    MemoryDeviceRepository, MemoryChannelRepository,
    MemorySubscriptionRepository, MemoryMessageRepository)
from instark.application.domain.common.query_parser import QueryParser
from instark.application.domain.services import MemoryDeliveryService
from instark.application.domain.common import (
    StandardTenantProvider, Tenant,
    StandardAuthProvider, User)


@fixture
def parser() -> QueryParser:
    return QueryParser()


@fixture
def auth_provider() -> StandardAuthProvider:
    auth_provider = StandardAuthProvider()
    auth_provider.setup(User(id='001', name='johndoe'))
    return auth_provider


@fixture
def tenant_provider() -> StandardTenantProvider:
    tenant_provider = StandardTenantProvider()
    tenant_provider.setup(Tenant(name="Default"))
    return tenant_provider


@fixture
def device_repository(tenant_provider, auth_provider):
    return MemoryDeviceRepository(
        QueryParser(), tenant_provider, auth_provider)


@fixture
def channel_repository(tenant_provider, auth_provider):
    return MemoryChannelRepository(
        QueryParser(), tenant_provider, auth_provider)


@fixture
def subscription_repository(tenant_provider, auth_provider):
    return MemorySubscriptionRepository(
        QueryParser(), tenant_provider, auth_provider)


@fixture
def message_repository(tenant_provider, auth_provider):
    return MemoryMessageRepository(
        QueryParser(), tenant_provider, auth_provider)


@fixture
def delivery_service():
    return MemoryDeliveryService()
