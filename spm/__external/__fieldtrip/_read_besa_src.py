from spm._runtime import Runtime


def _read_besa_src(*args, **kwargs):
    r"""
      READ_BESA_SRC reads a beamformer source reconstruction from a BESA file  
         
        Use as  
          [src] = read_besa_src(filename)  
         
        The output structure contains a minimal representation of the contents  
        of the file.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/read_besa_src.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_besa_src", *args, **kwargs)
