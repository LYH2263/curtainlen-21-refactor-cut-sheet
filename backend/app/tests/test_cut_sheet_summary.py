from app.engines.cut_sheet import build_sheet, total_meters


def test_sheet_length_and_running_total():
    sheet = build_sheet(5, 2.85)
    assert len(sheet) == 5
    assert [r["panel_index"] for r in sheet] == [1, 2, 3, 4, 5]
    assert sheet[-1]["running_meters"] == 14.25
    assert total_meters(sheet) == 14.25


def test_seed_living_room_blackout_totals():
    # 客厅落地窗 3.0x2.6 @2.0褶 x 遮光1.4m: 5 幅, 2.85m 裁高
    sheet = build_sheet(5, 2.6 + 0.10 + 0.15)
    assert total_meters(sheet) == 14.25


def test_empty_sheet_has_no_rows_and_zero_total():
    sheet = build_sheet(0, 2.85)
    assert sheet == []
    assert total_meters(sheet) == 0.0
    assert total_meters([]) == 0.0
