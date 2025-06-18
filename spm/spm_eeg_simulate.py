from mpython import Runtime


def spm_eeg_simulate(*args, **kwargs):
    """
      Simulate a number of MSP patches at specified locations on existing mesh
        function [Dnew,meshsourceind]=spm_eeg_simulate(D,prefix,patchmni,simsignal,ormni,woi,whitenoise,SNRdB,trialind,mnimesh,dipfwhm,nAmdipmom);
        D dataset
        prefix : prefix of new simulated dataset
        patchmni : patch centres in mni space or patch indices
        simsignal : Nsources x time series in nAm within woi
        woi: window of interest in seconds
        whitenoise level in rms femto Tesla or micro volts
        SNRdB power signal to noise ratio in dBs
        if neither whitenoise nor SNRdB are specified. defaults to whitenoise=10
        trialind: trials on which the simulated data will be added to the noise
        mnimesh : a new mesh with vertices in mni space
        dipfwhm - patch smoothness in mm, defaults to 0
        nAmdipmom- dipole moment in nAm, defaults to 10
        Outputs
        Dnew- new dataset
        meshsourceind- vertex indices of sources on the mesh
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_simulate.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_simulate", *args, **kwargs)
