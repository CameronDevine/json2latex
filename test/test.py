import unittest, json, re


class TestOutput(unittest.TestCase):
    def setUp(self):
        with open("test.json") as f:
            self.obj = json.load(f)
        with open("test.txt") as f:
            self.output = f.readlines()

    def test_output(self):
        for line in self.output:
            line = line.strip()
            if not line:
                continue

            if line.startswith("start"):
                self.assertEqual(line, "startend")
                continue

            attr, _, remainder = line.replace("”", '"').partition(":")
            attr = attr.strip()
            out = remainder.strip().strip("!")

            self.assertFalse(out.startswith(" "))
            self.assertFalse(out.endswith(" "))

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
                    self.assertEqual(json.loads(out), obj)
                    self.assertIsNone(re.search(",[^ ]", out), "At least one comma not followed by a space!")
                else:
                    self.assertEqual(str(obj), out)
                print(f"Tested attribute '{attr}' successfully.")

if __name__ == "__main__":
    unittest.main()
