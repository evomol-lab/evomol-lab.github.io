# GROMACS Post-Simulation Analysis Guide

After running your molecular dynamics simulation with GROMACS and obtaining 10 frames (`.gro` files), here are the commands to perform common analyses like RMSD, RMSF, and trajectory visualization.

## Prerequisites
First, you'll need to have:
1. Your original topology file (`.tpr`)
2. A compiled version of GROMACS (e.g., `gmx` or `gmx_mpi`)

## 1. Convert GRO files to XTC trajectory
Since you have separate GRO files, first combine them into a trajectory file:

```bash
# Combine GRO files into XTC trajectory
gmx trjcat -f step1.gro step2.gro step3.gro step4.gro step5.gro step6.gro step7.gro step8.gro step9.gro step10.gro -o trajectory.xtc
```

## 2. RMSD (Root Mean Square Deviation) Analysis
Calculate RMSD to assess structural stability:

```bash
# RMSD relative to first frame
gmx rms -s your_topology.tpr -f trajectory.xtc -o rmsd.xvg -tu ns

# RMSD relative to crystal/reference structure (if available)
gmx rms -s reference.pdb -f trajectory.xtc -o rmsd_ref.xvg -tu ns
```

When prompted:
- Select "Backbone" for protein backbone RMSD
- Or "Protein" for whole protein RMSD

## 3. RMSF (Root Mean Square Fluctuation) Analysis
Calculate RMSF to identify flexible regions:

```bash
gmx rmsf -s your_topology.tpr -f trajectory.xtc -o rmsf.xvg -res
```

When prompted, select the group you want to analyze (typically "Protein").

## 4. Visualization of Trajectories
To visualize your trajectory:

```bash
# Convert to PDB format (optional)
gmx trjconv -s your_topology.tpr -f trajectory.xtc -o trajectory.pdb

# Or visualize directly with VMD/Chimera/PyMOL
vmd your_topology.tpr trajectory.xtc
```

## 5. Other Useful Analyses

### Radius of Gyration
```bash
gmx gyrate -s your_topology.tpr -f trajectory.xtc -o gyrate.xvg
```

### Hydrogen Bonds Analysis
```bash
gmx hbond -s your_topology.tpr -f trajectory.xtc -num hbonds.xvg
```

### Secondary Structure Analysis (DSSP)
```bash
gmx do_dssp -f trajectory.xtc -s your_topology.tpr -o ss.xpm -sc ss.xvg
```

## Plotting Results
You can plot the `.xvg` files using `xmgrace` or Python (matplotlib):

```bash
xmgrace rmsd.xvg
```

Or in Python:
```python
import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('rmsd.xvg', comments=['#', '@'])
plt.plot(data[:,0], data[:,1])
plt.xlabel('Time (ns)')
plt.ylabel('RMSD (nm)')
plt.show()
```

## Notes
1. With only 10 frames, your analysis will be limited in statistical significance
2. For more meaningful results, consider running longer simulations (typically 100+ ns for proteins)
3. Always check your `.xvg` files for reasonable values before further analysis

Would you like me to elaborate on any specific analysis or provide more detailed commands for a particular part of the process?