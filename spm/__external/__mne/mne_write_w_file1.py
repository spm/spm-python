from mpython import Runtime


def mne_write_w_file1(*args, **kwargs):
    """
      mne_write_w_file1(filename, w)

         writes a binary 'w' file

         filename - name of file to write to
         w        - a structure with the following fields:

        vertices - vector of vertex indices (1-based)
        data     - vector of data values


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_write_w_file1.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_write_w_file1", *args, **kwargs)
