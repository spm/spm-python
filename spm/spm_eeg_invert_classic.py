from spm.__wrapper__ import Runtime


def spm_eeg_invert_classic(*args, **kwargs):
    """
      A trimmed down version of the spm_eeg_invert() routine  
        This version only handles single subject single modality data  
        The removal of many scaling factors makes it easier to compare between forward models  
        ReML inversion of multiple forward models for EEG-MEG  
        FORMAT [D] = spm_eeg_invert_classic(D)  
        ReML estimation of regularisation hyperparameters using the  
        spatiotemporal hierarchy implicit in EEG/MEG data  
         
        Requires:  
        D{i}.inv{val}.inverse:  
         
            inverse.modality - modality to use in case of multimodal datasets  
         
            inverse.trials - D.events.types to invert  
            inverse.type   - 'GS' Greedy search on MSPs  
                             'ARD' ARD search on MSPs  
                             'MSP' GS and ARD multiple sparse priors  
                             'LOR' LORETA-like model  
                             'IID' minimum norm  
                              'EBB' for empirical bayes beamformer  
            inverse.woi    - time window of interest ([start stop] in ms)  
            inverse.lpf    - band-pass filter - low frequency cut-off (Hz)  
            inverse.hpf    - band-pass filter - high frequency cut-off (Hz)  
            inverse.Han    - switch for Hanning window  
            inverse.xyz    - (n x 3) locations of spherical VOIs  
            inverse.rad    - radius (mm) of VOIs  
         
            inverse.Nm     - maximum number of channel modes  
            inverse.Nr     - maximum number of temporal modes  
            inverse.Np     - number of sparse priors per hemisphere  
            inverse.smooth - smoothness of source priors (0 to 1)  
            inverse.Na     - number of most energetic dipoles  
            inverse.sdv    - standard deviations of Gaussian temporal correlation  
            inverse.Qe     - any sensor error components (e.g. empty-room data)  
            inverse.Qe0     - minimum amount of sensor noise power relative to  
                               signal eg 0.1 would correspond to power SNR of 10.0  
            inverse.A       - predefined spatial modes (Nchans*Nmodes) to project  
                              sensor data through  
         
        Evaluates:  
         
            inverse.M      - MAP projector (reduced)  
            inverse.J{i}   - Conditional expectation (i conditions) J = M*U*Y  
            inverse.L      - Lead field (reduced UL := U*L)  
            inverse.qC     - spatial covariance  
            inverse.qV     - temporal correlations  
            inverse.T      - temporal projector  
            inverse.U(j)   - spatial projector (j modalities) - derived from data  
            inverse.A      - pre-specified spatial projector  
            inverse.Y{i}   - reduced data (i conditions) UY = UL*J + UE  
            inverse.Is     - Indices of active dipoles  
            inverse.It     - Indices of time bins  
            inverse.Ic{j}  - Indices of good channels (j modalities)  
            inverse.Nd     - number of dipoles  
            inverse.pst    - peristimulus time  
            inverse.dct    - frequency range  
            inverse.F      - log-evidence  
            inverse.VE     - variance explained in spatial/temporal subspaces (%)  
            inverse.R2     - variance in subspaces accounted for by model (%)  
            inverse.scale  - scaling of data for each of j modalities  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_invert_classic.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_invert_classic", *args, **kwargs)
