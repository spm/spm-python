from spm._runtime import Runtime


def _read_ctf_hist(*args, **kwargs):
    r"""
      READ_CTF_HIST  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/read_ctf_hist.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ctf_hist", *args, **kwargs)
