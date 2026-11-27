from spm._runtime import Runtime


def _write_stl(*args, **kwargs):
    r"""
      WRITE_STL writes a triangulation to an ASCII *.stl file, which is a file  
        format native to the stereolithography CAD software created by 3D Systems.  
         
        Use as  
          write_stl(filename, pos, tri, nrm)  
        where nrm refers to the triangle normals.  
         
        See also READ_STL  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/write_stl.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("write_stl", *args, **kwargs, nargout=0)
