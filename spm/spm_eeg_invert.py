from spm.__wrapper__ import Runtime


def spm_eeg_invert(*args, **kwargs):
    """
      ReML inversion of multiple forward models for EEG-MEG  
        FORMAT [D] = spm_eeg_invert(D, val)  
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
            inverse.pQ     - any source priors (e.g. from fMRI); vector or matrix  
            inverse.Qe     - any sensor error components (e.g. empty-room data)  
            inverse.dplot  - make diagnostics plots (0 or 1)  
            inverse.STAT   - flag for stationarity assumption, which invokes a   
                             full DCT temporal projector (from lpf to hpf Hz)  
         
        Evaluates:  
         
            inverse.M      - MAP projector (reduced)  
            inverse.J{i}   - Conditional expectation (i conditions) J = M*U*Y  
            inverse.L      - Lead field (reduced UL := U*L)  
            inverse.qC     - spatial covariance  
            inverse.qV     - temporal correlations  
            inverse.T      - temporal projector  
            inverse.U(j)   - spatial projector (j modalities)  
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
         
        1. This routine implements "group-based" inversion, corresponding to  
        ill-posed linear models of the following form:  
         
        [AY{1}...AY{n}] = L(1} * [J{1}...J{n}]   +  [e{1}...e{n}]  
         
        where AY{i} are the spatially normalized or adjusted data from subject i  
        that would have been seen if the lead-field L{i} = L{1}. The ensuing  
        Gaussian process priors on sources are then used to estimate subject-  
        specific MAP estimates of J{i} using  
         
        AY{i} = L(1} * J{i}  +  e{i}  
         
        using spatial priors from the group model above.  
         
        Here, A{i}  = L{1}*pinv(L{i}) =>  
              AY{i} = A(i}*L(i}*J{i}  
                    = L(1}*J{i}  
         
        Potential scaling differences between the lead-fields are handled by  
        scaling L{1} such that trace(L{1}*L{1}') = constant (number of spatial  
        modes or channels), while scaling the data such that trace(AY{n}*AY{n}') =  
        constant over subjects (and modalities; see below).  
         
        See: Electromagnetic source reconstruction for group studies.  
        Litvak V, Friston K.  
        NeuroImage. 2008 Oct 1;42(4):1490-8.  
         
       __________________________________________________________________________  
         
        2. It also implements "fusion" of different types of MEG and EEG data,  
        corresponding to ill-posed linear models of the following form:  
         
                    AY{1}{1,...,t}  = L(1} * J{1,...,t}   +  e{{1,...,t}}  
                    AY{2}{1,...,t}  = L(2}                   e{{2,...,t}}  
                         .  
                         .  
                         .  
                    AY{m}{1,...,t}  = L(n}                   e{{n,...,t}}  
         
        Under empirical priors on J{1,...,t} for m modalities with t trial types.  
         
        See: MEG and EEG data fusion: Simultaneous localisation of face-evoked  
        responses.  
        Henson R, Mouchlianitis E & Friston K.  
        Neuroimage. 2009. 47:581-9.  
       __________________________________________________________________________  
         
        3. It also allows incorporation of spatial source priors, eg, from fMRI  
        (see spm_eeg_inv_fmripriors.m). Note that if a vector is passed in  
        inverse.pQ, then variance components used (pass a matrix if a covariance  
        component is desired).  
         
        See: A Parametric Empirical Bayesian framework for fMRI-constrained  
        MEG/EEG source reconstruction.  
        Henson R, Flandin G, Friston K & Mattout J.  
        Human Brain Mapping. 2010. 1(10):1512-31.  
       __________________________________________________________________________  
         
        The routine essentially consists of two steps:  
         
          1. Optimisation of spatial source priors over subjects  
          2. Re-inversion of each subject, fusing across all modalities  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_invert.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_invert", *args, **kwargs)
