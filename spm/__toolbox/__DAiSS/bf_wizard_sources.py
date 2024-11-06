from spm.__wrapper__ import Runtime


def bf_wizard_sources(*args, **kwargs):
    """
      A handy command-line based batch filler with some defaults for DAiSS  
        source module, pick a few options, and it will default for unpopulated  
        fields  
         
        FORMAT [BF, batch, sources] = bf_wizard_sources(S)  
          S               - input structure  
        Optional fields of S:  
          S.BF            - Path to a BF structure or the  
                              structure itself  
                                                          - Default: REQUIRED  
         
          S.batch         - matlabbatch, of which this job  
                              can be appended to  
                                                          - Default: []  
         
          S.reduce_rank   - [1x2] vector determining the   
                            dimensionality of the lead  
                            fields for a source, first  
                            element for MEG, second for EEG  
                                                          - Default: [2 3]  
         
          S.keep3d        - If the leadfield rank has been  
                            reduced with S.reduce_rank, this  
                            ensures the are still 3 lead fields  
                            per source.                 
                                                          - Default: true  
         
          S.normalise_lf  - Make the norms of each lead field 1  
                                                          - Default: false  
          
          S.visualise     - Visualise the source space, sensors  
                            and conductive boundar[y/ies]  
                                                          - Default: true  
            
          S.method        - How do we want the source space  
                            generated? Validated methods with  
                            this are ( 'grid' | 'mesh' )     
                                                          - Default: REQUIRED  
         
          S.run           - Run the batch, set to 0 to  
                            bypass the run for debugging  
                                                          - Default: 1  
         
         
        Method options for S:  
        Extensive details can be found at   
        https://github.com/spm/spm/blob/main/toolbox/DAiSS/doc/commands/02_sources.md  
        But a summary of the essential options below.  
         
        GRID METHOD  
            
          S.grid.resolution - Distance between sources  
                               (in mm)                    - Default: 5  
         
          S.grid.constrain  - Which boundary do we want   
                              sources outside of to be  
                              excluded? Options: ('iskull'  
                              | 'oskull' | 'scalp')       - Default: 'iskull'  
         
        MESH METHOD  
         
         S.mesh.orient      - How are sources oriented on  
                              the vertices of the mesh?  
                              'unoriented' keeps the lead field  
                              triplet, whilst 'original' returns   
                              one lead field normal to the mesh  
                              surface  
                                                          - Default: 'unoriented'  
        Output:  
         BF               - Resultant DAiSS BF structure  
         batch            - matlabbatch job for spm_jobman to run  
         sources          - simplified summary of options selected  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_wizard_sources.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_wizard_sources", *args, **kwargs)
