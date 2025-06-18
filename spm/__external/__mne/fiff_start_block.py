from mpython import Runtime


def fiff_start_block(*args, **kwargs):
    """

        fiff_start_block(fid,kind)

        Writes a FIFF_BLOCK_START tag

            fid           An open fif file descriptor
            kind          The block kind to start


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_start_block.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_start_block", *args, **kwargs, nargout=0)
