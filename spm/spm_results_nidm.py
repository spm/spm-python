from spm.__wrapper__ import Runtime


def spm_results_nidm(*args, **kwargs):
    """
      Export SPM stats results using the Neuroimaging Data Model (NIDM)  
        FORMAT [nidmfile, prov] = spm_results_nidm(SPM,xSPM,TabDat,opts)  
        SPM      - structure containing analysis details (see spm_spm.m)  
        xSPM     - structure containing inference details (see spm_getSPM.m)  
        TabDat   - structure containing results details (see spm_list.m)  
        opts     - structure containing extra information about:  
          .group - subject/group(s) under study  
          .mod   - data modality  
          .space - reference space  
         
        nidmfile - output NIDM zip archive filename  
        prov     - provenance object (see spm_provenance.m)  
       __________________________________________________________________________  
        References:  
          
        Neuroimaging Data Model (NIDM):  
          http://nidm.nidash.org/  
         
        PROV-DM: The PROV Data Model:  
          http://www.w3.org/TR/prov-dm/  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_results_nidm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_results_nidm", *args, **kwargs)
