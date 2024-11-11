from spm.__wrapper__ import Runtime


def spm_dcm_phase(*args, **kwargs):
    """
      Estimate parameters of a DCM model of phase-coupled responses  
        FORMAT DCM = spm_dcm_phase(DCM)     
         
        DCM       
           name: name string  
              M:  Forward model  
                     M.dipfit - leadfield specification  
              xY: data   [1x1 struct]  
              xU: design [1x1 struct]  
         
          Sname: cell of source name strings  
         
          Connection constraints:  
         
              A: {[nr x nr double] }  
              B: {[nr x nr double]}   for GUI specification  
                                      (Nfourier=1 & only sine terms)  
          or  
         
              As: [nr x nr x Nfourier]  
              Ac: [nr x nr x Nfourier]  
              Bs: [nr x nr x Nfourier]     
              Bc: [nr x nr x Nfourier]   for script specification  
         
          options.type         - 'ECD'   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_phase.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_phase", *args, **kwargs)
