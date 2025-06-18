from mpython import Runtime


def spm_run_con(*args, **kwargs):
    """
      SPM job execution function - Specify and estimate contrasts
        Input:
        job    - harvested job data structure (see matlabbatch help)
        Output:
        out    - struct containing contrast and SPM{.} images filename
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_run_con.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_run_con", *args, **kwargs)
