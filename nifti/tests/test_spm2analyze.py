''' Tests for SPM2 header stuff '''

from volumeimages.spm2analyze import Spm2AnalyzeHeader

from test_spm99analyze import TestSpm99AnalyzeHeader

class TestSpm2AnalyzeHeader(TestSpm99AnalyzeHeader):
    header_class = Spm2AnalyzeHeader
    
