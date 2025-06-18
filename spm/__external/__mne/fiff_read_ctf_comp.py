from mpython import Runtime


def fiff_read_ctf_comp(*args, **kwargs):
    """

        [ compdata ] = fiff_read_ctf_comp(fid,node,chs,ch_rename)

        Read the CTF software compensation data from the given node


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_ctf_comp.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_ctf_comp", *args, **kwargs)
