from app.engines.cut_sheet import build_row


def test_row_fields_and_first_running():
    row = build_row(1, 2.85)
    assert row == {"panel_index": 1, "cut_height": 2.85, "running_meters": 2.85}


def test_row_accumulates_prior_meters():
    row = build_row(3, 2.85, prior_meters=5.7)
    assert row["panel_index"] == 3
    assert row["running_meters"] == 8.55


def test_row_rounds_cut_height_and_running():
    row = build_row(2, 2.8555, prior_meters=0.333)
    assert row["cut_height"] == 2.856
    assert row["running_meters"] == 3.19
