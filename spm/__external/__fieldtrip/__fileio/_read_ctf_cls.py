from spm.__wrapper__ import Runtime


def _read_ctf_cls(*args, **kwargs):
    """
      READ_CTF_CLS reads the classification file from a CTF dataset  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_cls.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ctf_cls", *args, **kwargs)
