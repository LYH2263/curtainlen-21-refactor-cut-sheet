import pytest
from app.engines.cut_sheet import CutSheetError, build_sheet, summarize_sheet


def test_seed_living_room_blackout():
    # 种子「客厅落地窗」×「遮光1.4m」默认褶量：与重构前一致 5 幅 / 14.25 m
    r = build_sheet(3.0, 2.6, 2.0, 0.10, 0.15, 1.4)
    assert r["panels"] == 5
    assert r["cut_height"] == 2.85
    assert r["meters"] == 14.25


def test_cut_sheet_rows_match_panels_and_total():
    r = build_sheet(3.0, 2.6, 2.0, 0.10, 0.15, 1.4)
    sheet = r["cut_sheet"]
    assert len(sheet) == r["panels"]
    assert [row["panel_index"] for row in sheet] == [1, 2, 3, 4, 5]
    assert all(row["cut_height"] == r["cut_height"] for row in sheet)
    assert sheet[-1]["running_meters"] == r["meters"]


def test_empty_sheet_summarizes_to_zero():
    r = summarize_sheet([])
    assert r["panels"] == 0
    assert r["meters"] == 0.0
    assert r["cut_sheet"] == []


def test_build_sheet_rejects_non_positive_width():
    with pytest.raises(CutSheetError):
        build_sheet(3.0, 2.6, 2.0, 0.10, 0.15, 0.0)
