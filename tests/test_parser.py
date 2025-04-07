from tree2structure.parser import parse_structure


raw = """
project/
├── src/
│   ├── main.py         # main logic
│   └── utils.py        # helper functions
├── tests/
│   └── test_main.py    # unit tests
└── README.md           # project overview
"""

expected = [
    {'folder': 'src/', 'files': [
        {'name': 'main.py', 'comment': '# main logic'},
        {'name': 'utils.py', 'comment': '# helper functions'}
    ]},
    {'folder': 'tests/', 'files': [
        {'name': 'test_main.py', 'comment': '# unit tests'}
    ]},
    {'folder': '.', 'files': [
        {'name': 'README.md', 'comment': '# project overview'}]
     }]


def test_parse_structure():
    result = parse_structure(raw)
    print(result)
    assert result == expected
