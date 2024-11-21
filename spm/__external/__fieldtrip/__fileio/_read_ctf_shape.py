from spm.__wrapper__ import Runtime


def _read_ctf_shape(*args, **kwargs):
    """
      READ_CTF_SHAPE reads headshape points and header information  
        from a CTF *.shape the accompanying *.shape_info file.  
         
        Use as  
          [shape] = read_ctf_shape(filename)  
        where filename should have the .shape extension  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_shape.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ctf_shape", *args, **kwargs)
