from aerbp.cli import main

def test_cli_main_prints_config(capsys):
    main()
    captured = capsys.readouterr()
    assert "AERBP Project Configuration:" in captured.out
    assert "raw_dir:" in captured.out
    assert "processed_dir:" in captured.out