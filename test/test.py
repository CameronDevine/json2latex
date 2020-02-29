import unittest, json


class TestOutput(unittest.TestCase):
    def setUp(self):
        with open("test.json") as f:
            self.obj = json.load(f)
        with open("test.txt") as f:
            self.output = f.readlines()

    def test_output(self):
        for line in self.output:
            if len(line.strip()) > 0:
                attr, out = line.strip().replace("”", '"').split(": ", 1)
                if attr == "x":
                    self.assertEqual(out, "??")
                else:
                    obj = self.obj
                    for el in attr.split("."):
                        if len(el) > 0:
                            if isinstance(obj, list):
                                obj = obj[int(el)]
                            else:
                                obj = obj[el]
                    if isinstance(obj, (list, dict)):
                        self.assertEqual(json.dumps(obj), out)
                    else:
                        self.assertEqual(str(obj), out)


if __name__ == "__main__":
    unittest.main()
