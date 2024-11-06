from spm.__wrapper__ import Runtime


def spm_dcm_virtual_electrodes(*args, **kwargs):
    """
      Posterior estimates of coupling among selected populations  
        FORMAT CSD = spm_dcm_virtual_electrodes(DCM,s,p,TYPE)  
         
        DCM  -  inverted DCM (see below)  
        s    -  indices of source, node or region  
        p    -  indices of population in node  
        TYPE -  {'CSD','CCF','DTF','GCA','COH','FSD'}  
         
        If called  with an output argument, graphics will be suppressed  
         
        Example:  
        >> spm_dcm_virtual_electrodes(DCM,[1,2,1],[1,1,8],'DTF')  
         
        Estimates:  
       --------------------------------------------------------------------------  
        DCM.dtf                   - directed transfer functions (source space)  
        DCM.ccf                   - cross covariance functions (source space)  
        DCM.coh                   - cross coherence functions (source space)  
        DCM.fsd                   - specific delay functions (source space)  
        DCM.pst                   - peristimulus time  
        DCM.Hz                    - frequency  
         
        DCM.Ep                    - conditional expectation  
        DCM.Cp                    - conditional covariance  
        DCM.Pp                    - conditional probability  
        DCM.Hc                    - conditional responses (y), channel space  
        DCM.Rc                    - conditional residuals (y), channel space  
        DCM.Hs                    - conditional responses (y), source space  
        DCM.Ce                    - ReML error covariance  
        DCM.F                     - Laplace log evidence  
        DCM.ID                    - data ID  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_virtual_electrodes.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_virtual_electrodes", *args, **kwargs)
