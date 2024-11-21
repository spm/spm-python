from spm.__wrapper__ import Runtime


def spm_dcm_tfm(*args, **kwargs):
    """
      Estimate parameters of a DCM of (induced) cross-spectral density  
        FORMAT DCM = spm_dcm_tfm(DCM)  
         
        DCM  
           name: name string  
              xY: data   [1x1 struct]  
              xU: design [1x1 struct]  
         
          Sname: cell of source name strings  
              A: {[nr x nr double], [nr x nr double], ...}  
              B: {[nr x nr double], ...}   Connection constraints  
              C: [nr x 1 double]  
         
          options.Nmodes       - number of spatial modes  
          options.h            - order of (DCT) detrending  
          options.Tdcm         - [start end] time window in ms  
          options.Fdcm         - [start end] Frequency window in Hz  
          options.D            - time bin decimation       (usually 1 or 2)  
          options.spatial      - 'ECD', 'LFP' or 'IMG'     (see spm_erp_L)  
         
        Returns:  
         
        sensor space  
       --------------------------------------------------------------------------  
        DCM.csd;                  % conditional cross-spectral density  
        DCM.tfm;                  % conditional induced responses  
        DCM.dtf;                  % conditional directed transfer functions  
        DCM.erp;                  % conditional evoked responses  
        DCM.Qu;                   % conditional neuronal responses  
        DCM.pst;                  % peristimulus times  
        DCM.Hz;                   % frequencies  
         
        store estimates in DCM  
       --------------------------------------------------------------------------  
        DCM.Ep;                   % conditional expectation - parameters  
        DCM.Cp;                   % conditional covariance  - parameters  
        DCM.Pp;                   % conditional probability - parameters  
        DCM.Ce;                   % error covariance  
        DCM.F;                    % Laplace log evidence  
        DCM.ID;                   % data ID  
         
        source space  
       --------------------------------------------------------------------------  
        DCM.CSD;                  % conditional cross-spectral density  
        DCM.TFM;                  % conditional induced responses  
        DCM.DTF;                  % conditional directed transfer functions  
        DCM.ERP;                  % conditional evoked responses  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_tfm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_tfm", *args, **kwargs)
