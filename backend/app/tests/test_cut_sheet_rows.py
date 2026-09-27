from app.engines.cut_sheet import build_row, build_rows


def test_first_row_running_equals_cut_height():
    row = build_row(1, 2.85)
    assert row == {"panel_index": 1, "cut_height": 2.85, "running_meters": 2.85}


def test_row_running_accumulates_by_index():
    row = build_row(5, 2.85)
    assert row["running_meters"] == 14.25


def test_row_cut_height_rounded_to_3():
    assert build_row(1, 2.850001)["cut_height"] == 2.85


def test_build_rows_sequential_indices():
    rows = build_rows(3, 2.0)
    assert [r["panel_index"] for r in rows] == [1, 2, 3]
    assert [r["running_meters"] for r in rows] == [2.0, 4.0, 6.0]


def test_build_rows_empty_when_no_panels():
    assert build_rows(0, 2.85) == []
