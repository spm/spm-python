from mpython import Runtime


def mne_load_coil_def(*args, **kwargs):
    """


          [CoilDef,Header] = mne_load_coil_def(fname);
          CoilDef          = mne_load_coil_def(fname);

          If file name is not specified, the standard coil definition file
          $MNE_ROOT/setup/mne/coil_def.dat or $MNE_ROOT/share/mne/coil_def.dat is read

          The content of the coil definition file is described in
          section 5.6 of the MNE manual

          This routine is modified from the original BrainStorm routine
          created by John C. Mosher


    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_load_coil_def.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_load_coil_def", *args, **kwargs)
