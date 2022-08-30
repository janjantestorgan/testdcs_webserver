import os

from tracker_dcs_web.utils.locate import abspath_root, abspath_data


def test_root():
    root = abspath_root()
    elements = os.listdir(root)
    assert {"tracker_dcs_web", "unittests"}.issubset(elements)


def test_data_path():
    dummy = abspath_data("dummy_files/test.txt")
    assert dummy.exists()
def open_data():
    with open("dummy_files/test.txt") as f:
        contents = f.readlines()
        # print(contents)
        result = {}
        n = {}  # pt100
        for x in contents:
            sublist = {}
            n["id"] = x.split("\t")[2]
            sublist["true_module"] = x.split("\t")[0]
            sublist["fake_module"] = x.split("\t")[1]
            n["modules"] = sublist  # 1. option
            # print(n)
            my_index = x.split("\t")[2]
            # print(my_index)
            result[int(my_index)] = sublist  # 2.option (turn string to int)

        f.close()
        print(result)
