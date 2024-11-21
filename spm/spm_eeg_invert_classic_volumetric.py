from spm.__wrapper__ import Runtime


def spm_eeg_invert_classic_volumetric(*args, **kwargs):
    """
      Volumetric multiple sparse priors  
        This version only handles single subject single modality data; the removal  
        of many scaling factors makes it easier to compare between forward models  
         
        Note also that this funtion performs a bit differently from the  
        spm_eeg_invert and spm_eeg_invert_classic functions. Namely:  
         
        1) No temporal filtering is carried out to the data by default  
        2) By default, each lead field element has one associated prior (i.e. no  
           "patches" or graph Laplacians are calculated).  
        3) Loreta-like priors/inversions are not (currently) supported.  
         
        Ryan Timms and Gareth Barnes, 2023.  
         
        Requires:  
                  An SPM object, D  
                  An inversion value, val  
         
        The usual SPM invert shenanigans applies:  
        D{i}.inv{val}.inverse:  
            inverse.modality - modality to use in case of multimodal datasets  
            inverse.trials - D.events.types to invert  
            inverse.type   - 'GS' Greedy search on MSPs  
                             'ARD' ARD search on MSPs  
                             'MSP' GS and ARD multiple sparse priors  
                             'IID' minimum norm  
                              'EBB' for empirical bayes beamformer  
            inverse.woi    - time window of interest ([start stop] in ms)  
            inverse.lpf    - band-pass filter - low frequency cut-off (Hz)  
            inverse.hpf    - band-pass filter - high frequency cut-off (Hz)  
            inverse.Han    - switch for Hanning window  
            inverse.Nm     - maximum number of channel modes  
            inverse.Nmax     - maximum number of temporal modes  
            inverse.Nt     - fixed/requested number of temporal modes  
            inverse.Np     - number of sparse priors per hemisphere  
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
         
        This version is for single subject single modality analysis and therefore  
        contains none of the associated scaling factors. No symmetric priors are  
        used in this implementation (just single patches) There is an option for  
        a Beamforming prior : inversion type 'EBB'.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_invert_classic_volumetric.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_invert_classic_volumetric", *args, **kwargs)
