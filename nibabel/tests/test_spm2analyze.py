''' Tests for SPM2 header stuff '''

import numpy as np

from nibabel.spm2analyze import Spm2AnalyzeHeader, Spm2AnalyzeImage

from nibabel.testing import assert_equal, assert_raises

import test_spm99analyze
from test_spm99analyze import _log_chk


class TestSpm2AnalyzeHeader(test_spm99analyze.TestSpm99AnalyzeHeader):
    header_class = Spm2AnalyzeHeader

    def test_spm_scale_checks(self):
        # checks for scale
        hdr = self.header_class()
        hdr['scl_slope'] = np.nan
        fhdr, message, raiser = _log_chk(hdr, 30)
        yield assert_equal(fhdr['scl_slope'], 1)
        problem_msg = ('no valid scaling in scalefactor '
                       '(=None) or cal / gl fields; '
                       'scalefactor assumed 1.0')
        yield assert_equal(message,
                           problem_msg + 
                           '; setting scalefactor "scl_slope" to 1')
        yield assert_raises(*raiser)
        dxer = self.header_class.diagnose_binaryblock
        yield assert_equal(dxer(hdr.binaryblock),
                           problem_msg)
        hdr['scl_slope'] = np.inf
        yield assert_equal(dxer(hdr.binaryblock),
                           problem_msg)


class TestSpm2AnalyzeImage(test_spm99analyze.TestSpm99AnalyzeImage):
    # class for testing images
    image_class = Spm2AnalyzeImage
    

def test_origin_affine():
    # check that origin affine works, only
    hdr = Spm2AnalyzeHeader()
    aff = hdr.get_origin_affine()
