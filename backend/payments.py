import stripe
from .settings import get_settings

settings = get_settings()
stripe.api_key = settings.stripe_api_key


def create_payment_intent(amount: int, currency: str, metadata: dict | None = None) -> tuple[str, str]:
    """Create a Stripe PaymentIntent and return its id and client secret."""
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        automatic_payment_methods={"enabled": True},
        metadata=metadata or {},
    )
    return intent.id, intent.client_secret
