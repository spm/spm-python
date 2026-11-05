from spm._runtime import Runtime


def _read_ctf_hdm(*args, **kwargs):
    r"""
      READ_CTF_HDM reads the head volume conductor model from a *.hdm file  
         
        vol = read_ctf_hdm(filename)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_ctf_hdm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ctf_hdm", *args, **kwargs)
