from spm.__wrapper__ import Runtime


def _write_off(*args, **kwargs):
    """
      WRITE_OFF writes a set of geometrical planar forms (called piecewise linear complex, PLC)  
        to an ascii *.off file, which is a file format created by Princeton Shape Benchmark  
         
        Use as  
          write_stl(filename, pnt, tri)  
         
        See also READ_OFF  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_off.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_off", *args, **kwargs, nargout=0)
