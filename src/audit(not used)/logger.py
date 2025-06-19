import logging

audit_logger = logging.getLogger("audit")

def log_action(user_id: int, action: str):
    audit_logger.info(f"User {user_id} performed action: {action}")
