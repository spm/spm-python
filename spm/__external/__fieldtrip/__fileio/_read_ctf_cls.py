from spm._runtime import Runtime


def _read_ctf_cls(*args, **kwargs):
    """
      READ_CTF_CLS reads the classification file from a CTF dataset  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_cls.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ctf_cls", *args, **kwargs)
