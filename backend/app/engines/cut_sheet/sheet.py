"""整单 sheet 汇总：由窗体/面料参数算出幅数与裁高，建行并汇总合计。"""
from app.engines.helpers import ceil_units
from app.engines.cut_sheet.rows import build_rows
from app.engines.cut_sheet.validation import require_valid_fabric_width


def summarize_sheet(rows: list, cut_height: float = 0.0, fabric_width: float = 0.0, finished_width: float = 0.0) -> dict:
    """把明细行汇总成整单结果；合计米数取末行 running_meters，空 sheet 为 0。"""
    rows = list(rows)
    return {
        "finished_width": round(float(finished_width), 3),
        "panels": len(rows),
        "cut_height": round(float(cut_height), 3),
        "meters": rows[-1]["running_meters"] if rows else 0.0,
        "fabric_width": float(fabric_width),
        "cut_sheet": rows,
    }


def build_sheet(window_w, window_h, fullness, hem_top, hem_bottom, fabric_width) -> dict:
    """整单裁幅明细：成品宽/门幅定幅数，层高加折边定裁高，逐幅建行后汇总。"""
    fw = require_valid_fabric_width(fabric_width)
    finished_w = float(window_w) * float(fullness)
    panels = max(1, ceil_units(finished_w / fw))
    cut_h = float(window_h) + float(hem_top) + float(hem_bottom)
    return summarize_sheet(build_rows(panels, cut_h), cut_h, fw, finished_w)
