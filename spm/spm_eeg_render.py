from spm.__wrapper__ import Runtime


def spm_eeg_render(*args, **kwargs):
    """
      Visualisation routine for the cortical surface  
        FORMAT [out] = spm_eeg_render(m,options)  
         
        INPUT:  
        m       - patch structure (with fields .faces et .vertices)  
                  or GIFTI format filename  
        options - structure with optional fields:  
                  .texture      - texture to be projected onto the mesh  
                  .clusters     - cortical parcellation (cell variable containing  
                                  the vertex indices of each cluster)   
                  .clustersName - name of the clusters  
                  .figname      - name to be given to the figure  
                  .ParentAxes   - handle of the axes within which the mesh should  
                                  be displayed  
                  .hfig         - handle of existing figure. If this option is  
                                  provided, then spm_eeg_render adds the (textured)  
                                  mesh to the figure hfig, and a control for its  
                                  transparency.  
         
        OUTPUT:  
        out     - structure with fields:  
                  .hfra    - frame structure for movie building  
                  .handles - structure containing the handles of the created  
                             uicontrols and mesh objects  
                  .m       - the structure used to create the mesh.  
       __________________________________________________________________________  
         
        This function is a visualisation routine, mainly for texture and  
        clustering on the cortical surface.  
        NB: The texture and the clusters cannot be visualised at the same time.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_render.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_render", *args, **kwargs)
