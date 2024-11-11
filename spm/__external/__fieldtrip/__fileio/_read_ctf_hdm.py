from spm.__wrapper__ import Runtime


def _read_ctf_hdm(*args, **kwargs):
    """
      READ_CTF_HDM reads the head volume conductor model from a *.hdm file  
         
        vol = read_ctf_hdm(filename)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_hdm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ctf_hdm", *args, **kwargs)
