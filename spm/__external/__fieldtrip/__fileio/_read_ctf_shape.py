from spm._runtime import Runtime


def _read_ctf_shape(*args, **kwargs):
    r"""
      READ_CTF_SHAPE reads headshape points and header information  
        from a CTF *.shape the accompanying *.shape_info file.  
         
        Use as  
          [shape] = read_ctf_shape(filename)  
        where filename should have the .shape extension  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_ctf_shape.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ctf_shape", *args, **kwargs)
