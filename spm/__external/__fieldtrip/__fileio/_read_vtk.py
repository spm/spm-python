from mpython import Runtime


def _read_vtk(*args, **kwargs):
    """
      READ_VTK reads a triangulation from a VTK (Visualisation ToolKit) format file.
        Supported are triangles, triangle strips, and other polygons.

        Use as
          [pnt, tri] = read_vtk(filename)

        See https://docs.vtk.org/en/latest/design_documents/VTKFileFormats.html
        and https://www.princeton.edu/~efeibush/viscourse/vtk.pdf

        See also WRITE_VTK, READ_VTK_XML


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_vtk.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_vtk", *args, **kwargs)
