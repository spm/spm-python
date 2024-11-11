from spm.__wrapper__ import Runtime


def spm_dcm_csd(*args, **kwargs):
    """
      Estimate parameters of a DCM of (complex) cross-spectral density  
        FORMAT DCM = spm_dcm_csd(DCM)  
         
        DCM  
           name: name string  
              xY: data   [1x1 struct]  
              xU: design [1x1 struct]  
         
          Sname: cell of source name strings  
              A: {[nr x nr double]  [nr x nr double]  [nr x nr double]}  
              B: {[nr x nr double], ...}   Connection constraints  
              C: [nr x 1 double]  
         
          options.Nmodes       - number of spatial modes  
          options.Tdcm         - [start end] time window in ms  
          options.Fdcm         - [start end] Frequency window in Hz  
          options.D            - time bin decimation       (usually 1 or 2)  
          options.spatial      - 'ECD', 'LFP' or 'IMG'     (see spm_erp_L)  
          options.model        - 'ERP', 'SEP', 'CMC', 'LFP', 'NMM' or 'MFM'  
         
        Esimates:  
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
        DCM.Ce                    - eML error covariance  
        DCM.F                     - Laplace log evidence  
        DCM.ID                    -  data ID  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_csd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_csd", *args, **kwargs)
