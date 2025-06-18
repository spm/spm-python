from mpython import Runtime


def spm_run_dcm_bms_vis(*args, **kwargs):
    """
      Review BMS results
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_run_dcm_bms_vis.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_run_dcm_bms_vis", *args, **kwargs)
