from mpython import Runtime


def mne_find_source_space_hemi(*args, **kwargs):
    """

        function mne_find_source_space_hemi(src)

        Return the hemisphere id for a source space

        src      - The source space to investigate
        hemi     - Deduced hemisphere id


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_find_source_space_hemi.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_find_source_space_hemi", *args, **kwargs)
