from app.engines.cut_sheet import build_sheet


def fabric_meters(
    window_w: float,
    window_h: float,
    fullness: float,
    hem_top: float,
    hem_bottom: float,
    fabric_width: float,
) -> dict:
    """兼容入口：裁幅明细已迁入 app.engines.cut_sheet，这里仅转发。"""
    return build_sheet(window_w, window_h, fullness, hem_top, hem_bottom, fabric_width)
