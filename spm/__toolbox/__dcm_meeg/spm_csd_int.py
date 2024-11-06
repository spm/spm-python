from spm.__wrapper__ import Runtime


def spm_csd_int(*args, **kwargs):
    """
      Time frequency response of a neural mass model  
        FORMAT [CSD,ERP,csd,mtf,w,pst,x,dP] = spm_csd_int(P,M,U)  
               ERP = spm_csd_int(P,M,U): M.ds = 0  
         
        P    - parameters  
        M    - neural mass model structure  
        M.ds - down-sampling for comutational efficiency (default = 1)  
               if ~M.ds then the ERP is returned  
        U    - time-dependent input  
         
        ERP  - {E(t,nc}}      - event-related average (sensor space)  
        CSD  - {Y(t,w,nc,nc}} - cross-spectral density for nc channels {trials}  
                              - for w frequencies over time t in M.Hz  
        csd  - {G(t,w,nc,nc}} - cross spectrum density (before sampling)  
        mtf  - {S(t,w,nc,nu}} - transfer functions  
        w    - frequencies  
        pst  - peristimulus time (sec)  
        x    - expectation of hidden (neuronal) states (for last trial)  
        dP   - {dP(t,np)}        - parameter fluctuations (plasticity)  
       __________________________________________________________________________  
         
        This integration routine evaluates the responses of a neural mass model  
        to exogenous input - in terms of neuronal states. These are then used as  
        expansion point to generate complex cross spectral responses due to  
        random neuronal fluctuations. The ensuing spectral (induced) response is  
        then convolved (in time) with a window that corresponds to the window of  
        a standard wavelet transform. In other words, this routine generates  
        predictions of data features based upon a wavelet transform  
        characterisation of induced responses.  
         
        If M.analysis = 'ERP' then only the ERP is evaluated  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_csd_int.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd_int", *args, **kwargs)
