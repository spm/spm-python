from spm.__wrapper__ import Runtime


def spm_eeg_simulate(*args, **kwargs):
    """
      Simulate a number of MSP patches at specified locations on existing mesh  
        FORMAT [Dnew,meshsourceind]=spm_eeg_simulate(D,prefix,patchmni,simsignal,woi,whitenoise,SNRdB,trialind,mnimesh,dipfwhm);  
        D dataset  
        prefix : prefix of new simulated dataset  
        patchmni : patch centres in mni space or patch indices  
        simsignal : Nsources x time series in nAm within woi  
        woi: window of interest in seconds  
        whitenoise level in rms femto Tesla or micro volts  
        SNRdB power signal to noise ratio in dBs  
        trialind: trials on which the simulated data will be added to the noise  
        mnimesh : a new mesh with vertices in mni space  
        dipfwhm - patch smoothness in mm  
         
        Outputs  
        Dnew- new dataset  
        meshsourceind- vertex indices of sources on the mesh  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_simulate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_simulate", *args, **kwargs)
