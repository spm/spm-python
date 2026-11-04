from spm._runtime import Runtime


def _read_vtk_xml(*args, **kwargs):
    r"""
      READ_VTK_XML reads a XML-formatted vtk file containing points in 3D and  
        connecting elements.  
         
        this function is a trial-and-error based implementation to read xml-style  
        vtk files. There is some documentation online, which seems somewhat  
        incomplete, or at least not fully understood by me.  
         
        See also READ_VTK, WRITE_VTK  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_vtk_xml.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_vtk_xml", *args, **kwargs)
