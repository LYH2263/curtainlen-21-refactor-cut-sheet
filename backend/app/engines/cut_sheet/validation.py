"""非法门幅/脏窗校验: reject unusable fabrics and windows before any math."""


class DirtyWindowError(ValueError):
    """Raised when a window is flagged dirty and must not be estimated."""


def require_positive_width(fabric_width) -> float:
    """Return the fabric width as float, rejecting missing/non-positive values."""
    try:
        width = float(fabric_width)
    except (TypeError, ValueError):
        raise ValueError("fabric width required")
    if width <= 0:
        raise ValueError("fabric width required")
    return width


def require_clean_window(window: dict) -> dict:
    """Return the window if usable, raising DirtyWindowError otherwise."""
    if not window:
        raise DirtyWindowError("dirty window")
    if window.get("data_quality") == "dirty":
        raise DirtyWindowError("dirty window")
    return window
