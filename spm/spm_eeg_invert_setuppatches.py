from spm.__wrapper__ import Runtime


def spm_eeg_invert_setuppatches(*args, **kwargs):
    """
      Set prior files for source inversion  
        FORMAT [Qp,Qe,allpriornames] = spm_eeg_invert_setuppatches(allIp,mesh,base,priordir,Qe,UL)  
        Each file contains  number of smooth patches on cortical surface a  
        allIp    - each row denotes a different prior file  
                   each column denotes the index of an impulse on the cortical surface  
        mesh     - cortical surface mesh (in metres)  
        base.nAm (optional)    - magnitude of the impulse.  
                                 There should be one value per column of Ip  
        base.smooth (optional) - FWHM smoothness of the impulse on cortical surface (in mm)  
        priordir - Directory in which the new priorfiles will be saved  
        Qe       - sensor level covariance  
        UL       - reduced lead field (only used to make a complete prior file)  
         
        Qp  - prior source covariances from prior created in last row of allIp  
        Qe  - prior sensor covariances  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_invert_setuppatches.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_invert_setuppatches", *args, **kwargs)
