import unittest

import utility


class TestUtility(unittest.TestCase):

    def test_sha256(self):
        """
        test sha256
        """
        self.assertEqual(
            utility.hasher("SHA256", "testing", False, None),
            "cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90",
        )
        self.assertEqual(
            utility.hasher("SHA256", "testing test", False, None),
            "83edb388910773f830671f7b48ef48006f134a713ec9d5d43aa3eb9f4dd4a07d",
        )

        # test salt
        self.assertEqual(
            utility.hasher("SHA256", "testing test", True, " test"),
            "994229ebe8537babe4e7b750344fb3e3a199632f41ec9537aa5e059bb912b6c2",
        )
        self.assertEqual(
            utility.hasher("SHA256", "testing test", True, " tester"),
            "68badaf405738b28f46ed8a8d545ee2362b21750c8822dc0499d3cb841b5787e",
        )

    def test_sha384(self):
        """
        test sha384
        """
        self.assertEqual(
            utility.hasher("SHA384", "fun test!!", False, None),
            "48d0a5753498b31177824dda40d1734518875dbb0ca847f388fded2729b43acab8be568016937cf4ed845a8aa0b150e6",
        )
        self.assertEqual(
            utility.hasher("SHA384", "fun test!! fun test!!", False, None),
            "078199f1fa96750ee6a6cae625f8aa7e634fc45802449b3a4f8456bcb2cb215b6d36abd5dd80c93c0ab221a96f2d7d6e",
        )

        # test salt
        self.assertEqual(
            utility.hasher("SHA384", "fun test!!", True, "salty salt"),
            "1db9581398f7a8a29797244b8ee6696d262dd375bc501b3ef9add1795efecbbe7862d0fdf42f9123e6e391645d37c42e",
        )
        self.assertEqual(
            utility.hasher("SHA384", "fun test!! fun test!!", True, "salty salt"),
            "b394c9604f5820367d05ea2a0b1c1b73769193e46fc75694cc023d8bee548215619f1df3a777fcd67310a8daddbdcbd4",
        )

    def test_sha512(self):
        """
        test sha512
        """
        self.assertEqual(
            utility.hasher("SHA512", "fun test!!", False, None),
            "25d920e0041c5097511a97b186dca5411e6e42557534fc749ad02c58d9dfd21895dd7d91bb7cc97c1dcb2abd9c14d0f5cc98a3237ef9501b256b8dd5145211da",
        )
        self.assertEqual(
            utility.hasher("SHA512", "fun test!! fun test!!", False, None),
            "5d54a34f1bf99c6963cfc649a38f507711ae1f28ed3c8935c2d4d2f4b8102934723358313b768a0cadd45d314d20c2d3916ad9d2c40b8b3cda809492b87ea7bf",
        )

        # test salt
        self.assertEqual(
            utility.hasher("SHA512", "fun test!!", True, "salty salt"),
            "40d9959f366a93241e0342f9fa06db132f6e96f76a01dfba05de665f0b0713eecb1e2d015f74819772b1bf4e4f0720faabeadbc661a1ac1e3fb02a50b3ccbe56",
        )
        self.assertEqual(
            utility.hasher("SHA512", "fun test!! fun test!!", True, "salty salt"),
            "f97be875091d8de46ab1de6aec773966ab42c33f8fca75741a7be90e44f5da2f71e182575832e2e09966b657ed98ab4d35cce133d4bbfc2db5f2b869b5434849",
        )

    def test_sha1(self):
        """
        test sha1
        """
        self.assertEqual(
            utility.hasher("SHA1", "fun test!!", False, None),
            "56347d2aa002d5cb38e632fe073d997ca844116b",
        )
        self.assertEqual(
            utility.hasher("SHA1", "fun test!! fun test!!", False, None),
            "2c294c65f355f533b4cdd7f03aca949941a18b6d",
        )

        # test salt
        self.assertEqual(
            utility.hasher("SHA1", "fun test!!", True, "salty salt"),
            "a814e9208ffdcea368f2ddff9cb0e9a2c21c2763",
        )
        self.assertEqual(
            utility.hasher("SHA1", "fun test!! fun test!!", True, "salty salt"),
            "f38fcd70ae47ba1c77e7f52a66c48444325c398c",
        )

    def test_md5(self):
        """
        test md5
        """
        self.assertEqual(
            utility.hasher("MD5", "fun test!!", False, None),
            "93c33de52005f4a3635d43f6de7782a0",
        )
        self.assertEqual(
            utility.hasher("MD5", "fun test!! fun test!!", False, None),
            "fff534d5d4ad7f3df01d519ba0a90be5",
        )

        # test salt
        self.assertEqual(
            utility.hasher("MD5", "fun test!!", True, "salty salt"),
            "a8b15866d384f993ffc6d0f584498704",
        )
        self.assertEqual(
            utility.hasher("MD5", "fun test!! fun test!!", True, "salty salt"),
            "757644ca06523bba1f1bf6b2574fd297",
        )


if __name__ == "__main__":
    unittest.main()
