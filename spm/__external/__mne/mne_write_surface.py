from mpython import Runtime


def mne_write_surface(*args, **kwargs):
    """

        mne_write_surface(fname,verts,faces)

        Writes a FreeSurfer surface file

        fname       - The file to write
        verts       - Vertex coordinates in meters
        faces       - The triangle descriptions
        comment     - Optional comment to include


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_write_surface.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_write_surface", *args, **kwargs, nargout=0)
