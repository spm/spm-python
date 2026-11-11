from spm._runtime import Runtime


def _read_ctf_mri4(*args, **kwargs):
    r"""
      READ_CTF_MRI reads header and imnage data from CTF format MRI file  
         
        [mri, hdr] = read_ctf_mri(filename)  
         
        See also READ_CTF_MEG4, READ_CTF_RES4  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_ctf_mri4.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ctf_mri4", *args, **kwargs)
