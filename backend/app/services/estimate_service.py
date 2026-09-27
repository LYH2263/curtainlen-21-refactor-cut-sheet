from fastapi import HTTPException
from app.engines.cut_sheet import CutSheetError, build_sheet, require_clean_window
from app.repositories import fabrics, history, settings_repo, windows

def run_estimate(window_id: int, fabric_id: int, save: bool, note: str):
    w = windows.get_window(window_id)
    f = fabrics.get_fabric(fabric_id)
    if not w or not f:
        raise HTTPException(404, "not found")
    settings = settings_repo.get_all()
    fullness = float(w.get("fullness") or settings.get("default_fullness", 2.0))
    try:
        require_clean_window(w)
        calc = build_sheet(w["width"], w["height"], fullness, f["hem_top"], f["hem_bottom"], f["fabric_width"])
    except CutSheetError as e:
        raise HTTPException(422, str(e))
    run_id = history.insert_run(window_id, fabric_id, calc, note) if save else None
    return {"window": w, "fabric": f, "run_id": run_id, **calc}
