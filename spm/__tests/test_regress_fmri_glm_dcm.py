from mpython import Runtime


def test_regress_fmri_glm_dcm(*args, **kwargs):
    """
      Regression test for GLM and DCM for fMRI including timseries extraction
        % This script analyses the Attention to Visual Motion fMRI dataset
        available from the SPM website using DCM:
          http://www.fil.ion.ucl.ac.uk/spm/data/attention/
        as described in the SPM docs website:
          https://www.fil.ion.ucl.ac.uk/spm/docs/tutorials/dcm/dcm_fmri_first_level_gui/
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_regress_fmri_glm_dcm.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_regress_fmri_glm_dcm", *args, **kwargs)
