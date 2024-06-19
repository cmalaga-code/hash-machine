import unittest

import utility


class TestUtility(unittest.TestCase):

    def test_sha256(self):
        """
        test sha256
        """
        self.assertEqual(
            utility.sha256("testing", False, None),
            "cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90")
        self.assertEqual(
            utility.sha256("testing test", False, None),
            "83edb388910773f830671f7b48ef48006f134a713ec9d5d43aa3eb9f4dd4a07d")

        # test salt
        self.assertEqual(
            utility.sha256("testing test", True, " test"),
            "994229ebe8537babe4e7b750344fb3e3a199632f41ec9537aa5e059bb912b6c2")
        self.assertEqual(
            utility.sha256("testing test", True, " tester"),
            "68badaf405738b28f46ed8a8d545ee2362b21750c8822dc0499d3cb841b5787e")


if __name__ == '__main__':
    unittest.main()
