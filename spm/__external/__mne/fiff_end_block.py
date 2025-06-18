from mpython import Runtime


def fiff_end_block(*args, **kwargs):
    """

        fiff_end_block(fid, kind)

        Writes a FIFF_BLOCK_END tag

            fid           An open fif file descriptor
            kind          The block kind to end


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_end_block.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_end_block", *args, **kwargs, nargout=0)
