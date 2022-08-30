import os

from tracker_dcs_web.utils.locate import abspath_root, abspath_data


def test_root():
    root = abspath_root()
    elements = os.listdir(root)
    assert {"tracker_dcs_web", "unittests"}.issubset(elements)


def test_data_path():
    dummy = abspath_data("dummy_files/test.txt")
    with open(dummy) as f:
        content = f.readlines()
        data = {}
        # n = {}  # pt100_id
        for x in content:
            sublist = {}
            # n["id"] = x.split("\t")[2]
            sublist["true_module"] = x.split("\t")[0]
            sublist["fake_module"] = x.split("\t")[1]
            # n["modules"] = sublist  # 1. option
            # print(n)
            data_index = x.split("\t")[2]
            data[int(data_index)] = sublist  # 2.option (turn string to int)

        f.close()
        print('reading data...')
        print(data)
    assert dummy.exists()
