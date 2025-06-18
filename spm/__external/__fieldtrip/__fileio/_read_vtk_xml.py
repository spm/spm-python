from mpython import Runtime


def _read_vtk_xml(*args, **kwargs):
    """
      READ_VTK_XML reads a XML-formatted vtk file containing points in 3D and
        connecting elements.

        this function is a trial-and-error based implementation to read xml-style
        vtk files. There is some documentation online, which seems somewhat
        incomplete, or at least not fully understood by me.

        See also READ_VTK, WRITE_VTK


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_vtk_xml.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_vtk_xml", *args, **kwargs)
