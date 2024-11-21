from spm.__wrapper__ import Runtime


def spm_MDP_VB_ERP(*args, **kwargs):
    """
      auxiliary routine for hierarchical electrophysiological responses  
        FORMAT [x,y] = spm_MDP_VB_ERP(MDP,FACTOR,T)  
         
        MDP    - structure (see spm_MDP_VB)  
        FACTOR - hidden factors (at high and low level) to plot  
        T      - flag to return cell of expectations (at time T; usually 1)  
         
        x      - simulated ERPs (high-level) (full lines)  
        y      - simulated ERPs (low level)  (dotted lines)  
        ind    - indices or bins at the end of each (synchronised) epoch  
         
        This routine combines first and second level hidden expectations by  
        synchronising them; such that first level updating is followed by an  
        epoch of second level updating - during which updating is suspended  
        (and expectations are held constant). The ensuing spike rates can be  
        regarded as showing delay period activity. In this routine, simulated  
        local field potentials are band pass filtered spike rates (between eight  
        and 32 Hz).  
         
        Graphics are provided for first and second levels, in terms of simulated  
        spike rates (posterior expectations), which are then combined to show  
        simulated local field potentials for both levels (superimposed).  
         
        At the lower level, only expectations about hidden states in the first  
        epoch are returned (because the number of epochs can differ from trial  
        to trial).  
         
        see also: spm_MDP_VB_LFP (for single level belief updating)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_VB_ERP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_VB_ERP", *args, **kwargs)
