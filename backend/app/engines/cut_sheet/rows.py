"""单幅行建造：一行 = 一幅的裁高与累计米数。"""


def build_row(panel_index: int, cut_height: float) -> dict:
    """建造第 panel_index 幅（1 起）的明细行。

    running_meters 为该幅裁完后的累计米数；等裁高下即 cut_height * panel_index，
    保证末行累计与整单合计同源。
    """
    idx = int(panel_index)
    h = float(cut_height)
    return {
        "panel_index": idx,
        "cut_height": round(h, 3),
        "running_meters": round(h * idx, 2),
    }


def build_rows(panels: int, cut_height: float) -> list:
    """按幅数建造连续明细行；panels <= 0 时为空 sheet。"""
    return [build_row(i, cut_height) for i in range(1, int(panels) + 1)]
