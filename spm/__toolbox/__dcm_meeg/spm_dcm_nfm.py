from spm._runtime import Runtime


def spm_dcm_nfm(*args, **kwargs):
    """
      Estimate parameters of a DCM of spectral neural field activity  
        FORMAT DCM = spm_dcm_nfm(DCM)  
         
        DCM  
           name: name string  
              M:  Forward model  
                     M.dipfit - lead-field specification  
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
          options.type         - 'ECD', 'LFP' or 'IMG'     (see spm_erp_L)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_nfm.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_nfm", *args, **kwargs)
