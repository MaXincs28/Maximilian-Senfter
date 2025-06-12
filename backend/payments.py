from uuid import uuid4


def create_payment_intent(amount: int, currency: str, metadata: dict | None = None) -> tuple[str, str]:
    """Return a dummy payment intent id and URL for local testing."""
    intent_id = uuid4().hex
    client_secret = f"http://localhost/payments/{intent_id}"
    return intent_id, client_secret
