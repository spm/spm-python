from spm.__wrapper__ import Runtime


def spm_fx_cmm_NMDA(*args, **kwargs):
    """
      State equations for canonical neural-mass and mean-field models  
        FORMAT [f,J,Q] = spm_fx_cmm(x,u,P,M)  
         
        x - states and covariances  
         
        x(i,j,k)        - k-th state of j-th population of i-th source  
                          i.e., running over sources, pop. and states  
         
          population: 1 - excitatory spiny stellate cells (input cells)  
                      2 - superficial pyramidal cells     (forward output cells)  
                      3 - inhibitory interneurons         (intrisic interneurons)  
                      4 - deep pyramidal cells            (backward output cells)  
         
               state: 1 V  - voltage  
                      2 gE - conductance (excitatory)  
                      3 gI - conductance (inhibitory)  
         
       --------------------------------------------------------------------------  
        refs:  
         
        Marreiros et al (2008) Population dynamics under the Laplace assumption  
         
        See also:  
         
        Friston KJ.  
        The labile brain. I. Neuronal transients and nonlinear coupling. Philos  
        Trans R Soc Lond B Biol Sci. 2000 Feb 29;355(1394):215-36.   
          
        McCormick DA, Connors BW, Lighthall JW, Prince DA.  
        Comparative electrophysiology of pyramidal and sparsely spiny stellate  
        neurons of the neocortex. J Neurophysiol. 1985 Oct;54(4):782-806.  
          
        Brunel N, Wang XJ.  
        What determines the frequency of fast network oscillations with irregular  
        neural discharges? I. Synaptic dynamics and excitation-inhibition  
        balance. J Neurophysiol. 2003 Jul;90(1):415-30.  
          
        Brunel N, Wang XJ.  
        Effects of neuromodulation in a cortical network model of object working  
        memory dominated by recurrent inhibition. J Comput Neurosci. 2001  
        Jul-Aug;11(1):63-85.  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fx_cmm_NMDA.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_cmm_NMDA", *args, **kwargs)
