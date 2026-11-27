from spm._runtime import Runtime


def _read_ctf_cls(*args, **kwargs):
    r"""
      READ_CTF_CLS reads the classification file from a CTF dataset  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_ctf_cls.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ctf_cls", *args, **kwargs)
