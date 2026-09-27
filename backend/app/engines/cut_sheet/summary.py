"""整单 sheet 汇总: assemble per-panel rows and order totals."""
from app.engines.cut_sheet.rows import build_row


def build_sheet(panels: int, cut_height: float) -> list:
    """One row per panel, running_meters accumulating across the order.

    panels <= 0 yields an empty sheet.
    """
    rows = []
    prior = 0.0
    for index in range(1, max(0, int(panels)) + 1):
        row = build_row(index, cut_height, prior)
        prior = row["running_meters"]
        rows.append(row)
    return rows


def total_meters(sheet: list) -> float:
    """Order total is the last row's running meters; an empty sheet totals 0."""
    if not sheet:
        return 0.0
    return sheet[-1]["running_meters"]
