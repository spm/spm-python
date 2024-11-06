from spm.__wrapper__ import Runtime


def _read_ctf_hist(*args, **kwargs):
    """
      READ_CTF_HIST  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/read_ctf_hist.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ctf_hist", *args, **kwargs)
