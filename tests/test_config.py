from aerbp.config import CONFIG, ensure_project_dirs, config_summary

def test_config_has_expected_directory_names():
    assert CONFIG.raw_dir.name == "raw"
    assert CONFIG.processed_dir.name == "processed"
    assert CONFIG.reports_dir.name == "reports"
    assert CONFIG.logs_dir.name == "logs"

def test_conig_summary_contains_core_keys():
    summary = config_summary()
    expected_keys = {
        "root", "raw_dir", "processed_dir", "reports_dir", "logs_dir",
        "db_path", "start_date", "end_date"
    }
    assert expected_keys.issubset(summary.keys())

def test_ensure_project_dirs_creates_directories():
    ensure_project_dirs()
    assert CONFIG.raw_dir.exists()
    assert CONFIG.processed_dir.exists()
    assert CONFIG.reports_dir.exists()
    assert CONFIG.logs_dir.exists()