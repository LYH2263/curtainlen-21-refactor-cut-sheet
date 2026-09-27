"""裁幅明细入参校验：非法门幅与脏窗。"""


class CutSheetError(ValueError):
    """裁幅明细的域内校验错误（继承 ValueError 以兼容既有调用方）。"""


def require_valid_fabric_width(fabric_width) -> float:
    """门幅必须可解析为正数，否则抛 CutSheetError。"""
    try:
        w = float(fabric_width)
    except (TypeError, ValueError):
        raise CutSheetError("fabric width required")
    if w <= 0:
        raise CutSheetError("fabric width required")
    return w


def require_clean_window(window: dict) -> dict:
    """脏窗（data_quality == 'dirty'）不得进入测算。"""
    if not window:
        raise CutSheetError("window required")
    if window.get("data_quality") == "dirty":
        raise CutSheetError("dirty window")
    return window
