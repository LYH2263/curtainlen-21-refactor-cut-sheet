import pytest

from app.engines.cut_sheet import (
    DirtyWindowError,
    require_clean_window,
    require_positive_width,
)


def test_zero_fabric_width_rejected():
    with pytest.raises(ValueError):
        require_positive_width(0)


def test_negative_fabric_width_rejected():
    with pytest.raises(ValueError):
        require_positive_width(-1.4)


def test_missing_fabric_width_rejected():
    with pytest.raises(ValueError):
        require_positive_width(None)


def test_valid_fabric_width_passes():
    assert require_positive_width("1.4") == 1.4


def test_dirty_window_rejected():
    with pytest.raises(DirtyWindowError):
        require_clean_window({"data_quality": "dirty"})


def test_clean_window_passes():
    w = {"data_quality": "clean", "width": 3.0}
    assert require_clean_window(w) is w
