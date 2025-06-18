from mpython import Runtime


def spm_eeg_inv_prep_modes_xval(*args, **kwargs):
    """
      Prepare a spatial mode file for inversion
       [spatialmodename,Nmodes,newpctest,testchans]=spm_eeg_inv_prep_modes_xval(filenames, Nmodes,...
           spatialmodename,Nblocks,pctest,gainmatfiles)
        this file ensures the same spatial modes are used across different files (which would contain the same data but different head-models for example)
        it also makes sure that the same channels groups are preserved to allow comparable cross validation and free energy metrics
        input a list of the M/EEG dataset names: filenames
        Nmodes - number of required spatial modes (if empty uses all available
        channels)
        spatialmodename- name of output file
        Nblocks- number of cross validation runs (optional and
        default 1)
        pctest- percentatge of channels to be used for testdata (optional and
        default 0)
        if pctest*Nblocks=100 then will use independent MEG channels and may adjust pctest (in output) to
        accommodate this. ( k-fold cross val)
        if pctest*Nblocks~=100 then uses random selection of pctest channels for each block (Monte-Carlo cross val)
        if gainmatfiles supplied uses these (rather than the one referenced by the spm
        object) to create unbiased(to any file) spatial modes matrix
        the output file (spatialmodename) will contain:
        megind- good meg channel indices
        testchans - indices to megind of channels to be turned off during training phase (and tested later)
        U{} - a different spatial modes matrix for each set of training channels or megind without indexed testchans or megind(setdiff(1:length(megind),testchans(b,:)))
        newpctest- the percentage of MEG channels actually used (need integer number of channels)
        testchans- which channels used for testing
        _________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_prep_modes_xval.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_prep_modes_xval", *args, **kwargs)
