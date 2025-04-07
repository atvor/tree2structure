from tree2structure.generator import create_from_structure


def test_create_from_structure(tmp_path):
    structure = [
        {
            "folder": "app",
            "files": [{"name": "main.py", "comment": "# main file"}],
            "subfolders": [
                {
                    "folder": "core",
                    "files": [{"name": "logic.py", "comment": "# core logic"}]
                }
            ]
        },
        {
            "folder": ".",
            "files": [{"name": "README.md", "comment": "# readme"}]
        }
    ]

    create_from_structure(structure, base_path=tmp_path)

    assert (tmp_path / "app" / "main.py").exists()
    assert (tmp_path / "app" / "core" / "logic.py").exists()
    assert (tmp_path / "README.md").exists()

    # Check contents
    with open(tmp_path / "README.md") as f:
        assert "# readme" in f.read()
