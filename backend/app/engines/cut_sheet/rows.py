"""单幅行建造: one cut-sheet row per panel."""


def build_row(panel_index: int, cut_height: float, prior_meters: float = 0.0) -> dict:
    """Build one cut-sheet row.

    panel_index is 1-based; running_meters accumulates this row's cut height
    on top of the meters used by all previous panels.
    """
    cut_h = round(float(cut_height), 3)
    return {
        "panel_index": int(panel_index),
        "cut_height": cut_h,
        "running_meters": round(float(prior_meters) + cut_h, 2),
    }
