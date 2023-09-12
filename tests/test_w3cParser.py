from logParser import W3CParser
import unittest
import numpy as np

class Test_w3cParser(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        cls.RAW_TEXT = [
            "#Software: Microsoft HTTP Server API 2.0  ",
            "#Version: 1.0   // the log file version as it's described by \"https://www.w3.org/TR/WD-logfile\".",
            "#Date: 2002-05-02 17:42:15  // when the first log file entry was recorded, which is when the entire log file was created.",
            "#Fields: date time c-ip cs-username s-ip s-port cs-method cs-uri-stem cs-uri-query sc-status cs(User-Agent)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/index.html - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/index.html - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /cats - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)"
        ]
        cls.RAW_DATA = [
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/index.html - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/index.html - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /images/picture.jpg - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)",
            "2002-05-02 17:42:15 172.22.255.255 - 172.30.255.255 80 GET /cats - 200 Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)"
        ]
        cls.NP_ARRAY = np.array([
            ["2002-05-02", "17:42:15", "172.22.255.255", "-", "172.30.255.255", "80", "GET", "/images/picture.jpg", "-", "200", "Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)"],
            ["2002-05-02", "17:42:15", "172.22.255.255", "-", "172.30.255.255", "80", "GET", "/images/picture.jpg", "-", "200", "Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)"],
            ["2002-05-02", "17:42:15", "172.22.255.255", "-", "172.30.255.255", "80", "GET", "/images/index.html", "-", "200", "Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)"],
            ["2002-05-02", "17:42:15", "172.22.255.255", "-", "172.30.255.255", "80", "GET", "/images/picture.jpg", "-", "200", "Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)"],
            ["2002-05-02", "17:42:15", "172.22.255.255", "-", "172.30.255.255", "80", "GET", "/images/picture.jpg", "-", "200", "Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)"],
            ["2002-05-02", "17:42:15", "172.22.255.255", "-", "172.30.255.255", "80", "GET", "/images/index.html", "-", "200", "Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)"],
            ["2002-05-02", "17:42:15", "172.22.255.255", "-", "172.30.255.255", "80", "GET", "/images/picture.jpg", "-", "200", "Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)"],
            ["2002-05-02", "17:42:15", "172.22.255.255", "-", "172.30.255.255", "80", "GET", "/images/picture.jpg", "-", "200", "Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)"],
            ["2002-05-02", "17:42:15", "172.22.255.255", "-", "172.30.255.255", "80", "GET", "/cats", "-", "200", "Mozilla/4.0+(compatible;MSIE+5.5;+Windows+2000+Server)"]
        ])
        cls.parser = W3CParser()
        cls.parser._rawText = cls.RAW_TEXT
        
    def test_get_raw_data(self):
        self.assertEqual(self.parser.getRawData(), self.RAW_DATA)

    def test_get_fields(self):
        self.assertEqual(
            self.parser.getFields(),
            [
                "date",
                "time",
                "c-ip",
                "cs-username",
                "s-ip",
                "s-port",
                "cs-method",
                "cs-uri-stem",
                "cs-uri-query",
                "sc-status",
                "cs(User-Agent)"
            ])
        
    def test_get_2d_data(self):
        np.testing.assert_array_equal(self.parser.get2dDataArray(), self.NP_ARRAY)

    def test_count_in_field(self):
        self.assertEqual(
            self.parser.countInField('cs-uri-stem'),
            {
                '/images/picture.jpg': 6,
                '/images/index.html': 2,
                '/cats': 1
            })