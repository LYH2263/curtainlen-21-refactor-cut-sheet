import pytest
from app.engines.cut_sheet import CutSheetError, require_clean_window, require_valid_fabric_width


def test_fabric_width_zero_rejected():
    with pytest.raises(CutSheetError):
        require_valid_fabric_width(0)


def test_fabric_width_negative_rejected():
    with pytest.raises(CutSheetError):
        require_valid_fabric_width(-1.4)


def test_fabric_width_non_numeric_rejected():
    with pytest.raises(CutSheetError):
        require_valid_fabric_width("abc")


def test_fabric_width_none_rejected():
    with pytest.raises(CutSheetError):
        require_valid_fabric_width(None)


def test_fabric_width_positive_passes():
    assert require_valid_fabric_width("1.4") == 1.4


def test_error_is_value_error_compatible():
    with pytest.raises(ValueError):
        require_valid_fabric_width(0)


def test_dirty_window_rejected():
    with pytest.raises(CutSheetError, match="dirty window"):
        require_clean_window({"id": 3, "data_quality": "dirty"})


def test_clean_window_passes():
    w = {"id": 1, "data_quality": "clean"}
    assert require_clean_window(w) is w


def test_missing_window_rejected():
    with pytest.raises(CutSheetError):
        require_clean_window(None)
