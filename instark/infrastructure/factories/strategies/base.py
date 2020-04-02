base = {
    # --- PROVIDERS ---
    "QueryParser": {
        "method": "query_parser"
    },
    "TenantProvider": {
        "method": "standard_tenant_provider"
    },
    "AuthProvider": {
        "method": "standard_auth_provider"
    },
    "TransactionManager": {
        "method": "memory_transaction_manager"
    },
    # --- REPOSITORIES ---
    "ChannelRepository": {
        "method": "memory_channel_repository"
    },
    "DeviceRepository": {
        "method": "memory_device_repository"
    },
    "MessageRepository": {
        "method": "memory_message_repository"
    },
    "SubscriptionRepository": {
        "method": "memory_subscription_repository"
    },
    # --- COORDINATORS ---
    "NotificationCoordinator": {
        "method": "notification_coordinator"
    },
    "RegistrationCoordinator": {
        "method": "registration_coordinator"
    },
    "SessionCoordinator": {
        "method": "session_coordinator"
    },
    "SubscriptionCoordinator": {
        "method": "subscription_coordinator"
    },
    # --- INFORMERS ---
    "InstarkInformer": {
        "method": "standard_instark_informer"
    },
    # --- SUPPLIERS ---
    "TenantSupplier": {
        "method": "memory_tenant_supplier"
    },
    "SetupSupplier": {
        "method": "memory_setup_supplier"
    },
    # --- SERVICES ---
    "DeliveryService": {
        "method": "memory_delivery_service"
    },
}