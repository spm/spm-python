from spm._runtime import Runtime


def _read_mff_bin(*args, **kwargs):
    r"""
      READ_MFF_BIN  
         
        Use as  
          [hdr] = read_mff_bin(filename)  
        or  
          [dat] = read_mff_bin(filename, begblock, endblock);  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_mff_bin.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_mff_bin", *args, **kwargs)
