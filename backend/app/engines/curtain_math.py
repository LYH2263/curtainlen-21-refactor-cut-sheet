from app.engines.cut_sheet import build_sheet, require_positive_width, total_meters
from app.engines.helpers import ceil_units


def fabric_meters(
    window_w: float,
    window_h: float,
    fullness: float,
    hem_top: float,
    hem_bottom: float,
    fabric_width: float,
) -> dict:
    width = require_positive_width(fabric_width)
    finished_w = float(window_w) * float(fullness)
    panels = max(1, ceil_units(finished_w / width))
    cut_h = float(window_h) + float(hem_top) + float(hem_bottom)
    sheet = build_sheet(panels, cut_h)
    return {
        "finished_width": round(finished_w, 3),
        "panels": panels,
        "cut_height": round(cut_h, 3),
        "meters": total_meters(sheet),
        "fabric_width": width,
        "cut_sheet": sheet,
    }
