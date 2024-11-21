from spm.__wrapper__ import Runtime


def spm_mar_spectra(*args, **kwargs):
    """
      Get spectral estimates from MAR model  
        FORMAT [mar] = spm_mar_spectra (mar,freqs,ns,show)  
         
        mar   - MAR data structure (see spm_mar.m)  
        freqs - [Nf x 1] vector of frequencies to evaluate spectra at  
        ns    - samples per second (default: ns = 2*freqs(end))  
        show  - 1 if you wish to plot estimates (default is 0)  
         
        The returned mar will have the following fields specified:  
         
        .P     [Nf x d x d] Power Spectral Density matrix  
        .H     [Nf x d x d] Transfer Function matrix  
        .C     [Nf x d x d] Coherence matrix  
        .dtf   [Nf x d x d] Kaminski's Directed Transfer Function matrix  
        .pve   [Nf x d x d] Geweke's proportion of variance explained  
        .gew   [Nf x d x d] Geweke's frequency domain Granger causality  
        .pdc   [Nf x d x d] Baccala's Partial Directed Coherence  
        .L     [Nf x d x d] Phase matrix  
        .f     [Nf x 1] Frequency vector  
        .ns    Sample rate  
         
        dtf(f,i,j) is the DTF at frequency f from signal j to signal i  
        pdc(f,i,j) is the PDC at frequency f from signal j to signal i  
        pve(f,i,j) is the proportion of power in signal i at frequency f that can  
                   be predicted by signal j.   
        gew(f,i,j) is the Granger casuality from signal j to signal i at frequency f.  
                   gew=-log(1-pev)  
         
        For DTF and PDC see L. Baccala and K. Sameshima (2001) Biol Cyb 84, 463-474.  
        For PVE and GEW see A. Brovelli et al. (2004) PNAS 101(26) 9849-9854.  
         
        In addition to the definition of PDC in the above paper, in this  
        implementation PDC is also scaled by the observation noise variance  
        (Baccala, personal communication).  
         
        Also note that PVE and GEW are only valid for d=2 time series  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_mar_spectra.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mar_spectra", *args, **kwargs)
