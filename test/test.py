import unittest, json


class TestOutput(unittest.TestCase):
    def setUp(self):
        with open("test.json") as f:
            self.obj = json.load(f)
        with open("test.txt") as f:
            self.output = f.readlines()

    def test_output(self):
        lines_iter = iter(self.output)
        for line in lines_iter:
            line = line.strip()
            if not line:
                continue
            # Only process lines starting with \def (a macro)
            if not line.startswith("\\def"):
                continue

            # Split macro name from first `{`
            attr, remainder = line.replace("”", '"').split("{", 1)

            # Collect all lines until the closing '}%'
            macro_lines = [remainder]
            while not macro_lines[-1].endswith("}%"):
                macro_lines.append(next(lines_iter).strip())

            # Join macro lines into a single string
            out = "".join(l.rstrip("%") for l in macro_lines)

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
