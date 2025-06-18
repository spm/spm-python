from mpython import Runtime


def mne_read_morph_map(*args, **kwargs):
    """

        [leftmap,rightmap] = mne_read_morph_map(from,to,subjects_dir)

        Read the morphing map from subject 'from' to subject 'to'.
        If subjects_dir is not specified, the SUBJECTS_DIR environment
        variable is used


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_read_morph_map.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_morph_map", *args, **kwargs)
