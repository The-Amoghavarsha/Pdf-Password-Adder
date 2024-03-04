import unittest
from unittest.mock import patch
import pdf_password_adder

class TestPDFPasswordAdder(unittest.TestCase):

    @patch('pdf_password_adder.filedialog.askopenfilename', return_value='/path/to/sample.pdf')
    def test_select_pdf_file(self, mock_askopenfilename):
        pdf_password_adder.select_pdf_file()
        self.assertEqual(pdf_password_adder.entry_pdf.get(), '/path/to/sample.pdf')

if __name__ == '__main__':
    unittest.main()

